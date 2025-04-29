# back_end/api/dependencies/auth.py

"""
Authentication dependency for FastAPI routes using AWS Cognito.

This module defines the `get_current_user` function, which:
- Extracts and verifies the JWT access token from the Authorization header.
- Validates the token against AWS Cognito's JWKs.
- Returns the decoded payload if valid.

Environment variables are loaded from `.env.cognito`:
- COGNITO_REGION
- COGNITO_USER_POOL_ID
- COGNITO_CLIENT_ID (optional: used to verify the `aud` claim)
"""

import os
import logging
from dotenv import load_dotenv
from fastapi import Request, HTTPException, status
from jwt import PyJWKClient, decode as jwt_decode, InvalidTokenError

# Load Cognito-related environment variables (useful for Uvicorn reloads)
load_dotenv(dotenv_path="env_folder/.env.cognito")

# Setup logger for this module
logger = logging.getLogger("auth")
logger.setLevel(logging.DEBUG)

# Read environment variables
COGNITO_REGION = os.getenv("COGNITO_REGION")
USER_POOL_ID = os.getenv("COGNITO_USER_POOL_ID")
APP_CLIENT_ID = os.getenv("COGNITO_CLIENT_ID")  # Optional (used if you enable verify_aud)

# Check required variables
if not COGNITO_REGION or not USER_POOL_ID:
    raise RuntimeError("❌ COGNITO_REGION and COGNITO_USER_POOL_ID must be set in environment variables")

# Cognito URLs
COGNITO_ISSUER = f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/{USER_POOL_ID}"
JWK_URL = f"{COGNITO_ISSUER}/.well-known/jwks.json"


async def get_current_user(request: Request):
    """
    FastAPI dependency to verify and decode a JWT token from the request.

    Args:
        request (Request): The FastAPI request object containing headers.

    Returns:
        dict: The decoded JWT payload if valid.

    Raises:
        HTTPException: 401 if token is missing or invalid.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        logger.warning("🚫 Missing or malformed Authorization header.")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing Authorization header")

    token = auth_header.removeprefix("Bearer ").strip()

    try:
        logger.debug("🔐 Fetching JWK from: %s", JWK_URL)
        jwk_client = PyJWKClient(JWK_URL)
        signing_key = jwk_client.get_signing_key_from_jwt(token)

        decoded_token = jwt_decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            issuer=COGNITO_ISSUER,
            options={"verify_aud": False},  # Set to True if using aud validation
        )

        logger.info("✅ Token valid. User sub: %s", decoded_token.get("sub"))
        return decoded_token

    except InvalidTokenError as e:
        logger.error("❌ Invalid token: %s", str(e))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token: {str(e)}")

    except Exception as e:
        logger.exception("❌ Unexpected error while verifying token.")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Token verification error: {str(e)}")