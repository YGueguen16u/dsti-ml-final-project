# models/nlp/s3_nlp_controller.py

"""
This module provides a reusable controller for managing S3 operations
related to NLP training, such as uploading and downloading any file
within the NLP folder structure of the configured bucket.
"""

from .s3_nlp_manager import S3NLPManager


class S3NLPController:
    """
    A high-level controller to interact with S3 storage for NLP workflows.

    Supports upload/download of any file by specifying custom paths.
    """

    def __init__(self):
        """
        Initializes the controller by creating an instance of S3NLPManager.
        """
        self.manager = S3NLPManager()

    def upload(self, local_path: str, s3_key: str):
        """
        Uploads a local file to the NLP folder in the S3 bucket.

        Args:
            local_path (str): Path to the file on the local filesystem.
            s3_key (str): Destination path in S3 (e.g., "nlp/datasets/my_file.jsonl").
        """
        print(f"🚀 Uploading {local_path} → s3://{s3_key}")
        self.manager.upload_dataset(local_path, s3_key)
        print(f"✅ Upload complete: {s3_key}\n")

    def download(self, s3_key: str, local_path: str):
        """
        Downloads a file from the S3 NLP folder to the local system.

        Args:
            s3_key (str): Path in S3 (e.g., "nlp/outputs/result.json").
            local_path (str): Destination path on the local filesystem.
        """
        print(f"📥 Downloading s3://{s3_key} → {local_path}")
        self.manager.download_predictions(s3_key, local_path)
        print(f"✅ Download complete: {local_path}\n")

    def list_files(self, prefix="nlp/"):
        """
        Lists all files in the S3 NLP folder or under a subfolder prefix.

        Args:
            prefix (str): Folder path in S3 to search in (default: "nlp/").

        Returns:
            List[str]: List of S3 keys found under the prefix.
        """
        print(f"📂 Listing files in s3://{prefix}")
        return self.manager.list_dataset_files(prefix)
