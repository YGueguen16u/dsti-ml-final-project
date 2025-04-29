# models/nlp/s3_nlp_manager.py

"""
This module provides a high-level interface to interact with AWS S3 for NLP-specific tasks,
such as uploading fine-tuning datasets, downloading model predictions, or listing files.
"""

from infrastructure.aws.s3.s3_manager import S3Manager

class S3NLPManager:
    def __init__(self):
        self.s3_manager = S3Manager()

    def upload_dataset(self, local_path, s3_key):
        """
        Upload a dataset to S3 from the local file system.
        """
        self.s3_manager.upload(local_path, s3_key)

    def download_predictions(self, s3_key, local_path):
        """
        Download NLP model predictions from S3 to the local system.
        """
        self.s3_manager.download(s3_key, local_path)

    def list_dataset_files(self, prefix="nlp/datasets/"):
        """
        List all dataset files in S3 under the specified prefix.
        """
        return self.s3_manager.list(prefix)
