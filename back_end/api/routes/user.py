# back_end/api/routes/user.py

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from back_end.api.dependencies.auth import get_current_user
from back_end.database.repository.user_repository import UserRepository
from back_end.database.connect import DatabaseConnector
from back_end.config.settings import settings
import traceback
import uuid

# Crée une instance propre de DatabaseConnector
db_connector = DatabaseConnector(database_url=settings.DATABASE_URL)

router = APIRouter(prefix="/api/user", tags=["User"])


@router.get("/me")
def get_me(user=Depends(get_current_user)):
    """Retourne les informations basiques de l'utilisateur connecté."""
    return {
        "email": user.get("email"),
        "sub": user.get("sub"),
        "groups": user.get("cognito:groups", [])
    }


class UserProfile(BaseModel):
    age: int
    weight: float
    target_weight: float
    height: float
    gender: str
    diet_type: str
    fitness_level: str
    goals: list[str]


@router.post("/profile")
def create_profile(profile: UserProfile, db: Session = Depends(db_connector.get_db)):
    """Crée un profil utilisateur dans PostgreSQL."""
    try:
        repo = UserRepository(db)
        user_id = str(uuid.uuid4())  # Création UUID ici si pas Cognito

        new_user_id = repo.insert_user(
            user_id=user_id,
            age=profile.age,
            gender=profile.gender,
            height=profile.height,
            weight=profile.weight,
            target_weight=profile.target_weight,
            diet_type=profile.diet_type,
            fitness_level=profile.fitness_level,
            goals=profile.goals
        )

        return {"message": "Profil créé", "user_id": new_user_id}

    except Exception:
        print("❌ ERREUR lors de l'insertion du profil :")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Erreur interne lors de l'enregistrement du profil")


@router.get("/all")
def list_all_users(db: Session = Depends(db_connector.get_db)):
    """Liste tous les utilisateurs enregistrés."""
    try:
        repo = UserRepository(db)
        users = repo.get_all_users()

        return users

    except Exception:
        print("❌ ERREUR lors de la récupération des utilisateurs :")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Erreur interne lors de la récupération des utilisateurs")