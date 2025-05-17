# Infrastructure/aws/s3/s3_manager.py

import json

import boto3
from botocore.exceptions import ClientError, NoCredentialsError
from infrastructure.aws.s3.config import get_s3_config

class S3Manager:
    """
    A manager class for interacting with an AWS S3 bucket.

    Provides methods for uploading, downloading, listing, and deleting files.
    Credentials and bucket configuration are automatically loaded from .env.
    """

    def __init__(self):
        """
        Initializes the S3Manager with AWS credentials and bucket info
        loaded from the environment (via get_s3_config).
        """
        config = get_s3_config()
        self.bucket = config["bucket"]
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=config["access_key"],
            aws_secret_access_key=config["secret_key"],
            region_name=config["region"]
        )

    def upload(self, local_path: str, s3_key: str):
        """
        Uploads a local file to the S3 bucket.

        Args:
            local_path (str): Path to the file on the local filesystem.
            s3_key (str): Path (key) where the file should be stored in S3.

        Returns:
            None
        """
        try:
            self.s3.upload_file(local_path, self.bucket, s3_key)
            print(f"Uploaded: {local_path} → s3://{self.bucket}/{s3_key}")
        except FileNotFoundError:
            print("File not found:", local_path)
        except NoCredentialsError:
            print("AWS credentials not found!")

    def download(self, s3_key: str, local_path: str):
        """
        Downloads a file from the S3 bucket to the local filesystem.

        Args:
            s3_key (str): The path (key) of the file in S3.
            local_path (str): Path to store the downloaded file locally.

        Returns:
            None
        """
        try:
            self.s3.download_file(self.bucket, s3_key, local_path)
            print(f"Downloaded: s3://{self.bucket}/{s3_key} → {local_path}")
        except ClientError as e:
            print(f"Error: {e}")

    def list(self, prefix: str = ""):
        """
        Lists all files (keys) in the S3 bucket under the given prefix.

        Args:
            prefix (str): (Optional) The S3 folder path to filter files.

        Returns:
            List[str]: A list of keys (file paths) in the bucket.
        """
        try:
            response = self.s3.list_objects_v2(Bucket=self.bucket, Prefix=prefix)
            files = [obj["Key"] for obj in response.get("Contents", [])]
            print(f" Files in s3://{self.bucket}/{prefix}:")
            for f in files:
                print(" -", f)
            return files
        except Exception as e:
            print(f"Error listing files: {e}")
            return []

    def load_json(self, s3_key: str):
        """
        Loads a JSON file directly from S3 and parses it.

        Args:
            s3_key (str): The path (key) of the JSON file in the S3 bucket.

        Returns:
            dict or list: Parsed JSON content, or [] in case of error.
        """
        try:
            response = self.s3.get_object(Bucket=self.bucket, Key=s3_key)
            content = response["Body"].read().decode("utf-8")
            return json.loads(content)
        except Exception as e:
            print(f"Failed to load JSON from s3://{self.bucket}/{s3_key} — {e}")
            return []


    def delete(self, s3_key: str):
        """
        Deletes a file from the S3 bucket.

        Args:
            s3_key (str): Path (key) of the file to delete in S3.

        Returns:
            None
        """
        try:
            self.s3.delete_object(Bucket=self.bucket, Key=s3_key)
            print(f" Deleted: s3://{self.bucket}/{s3_key}")
        except ClientError as e:
            print(f"Error deleting file: {e}")