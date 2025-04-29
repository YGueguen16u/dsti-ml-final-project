# tests/infrastructure/aws/s3/test_s3_manager.py

"""
Unit tests for the S3Manager class using mocked boto3 client.

These tests validate the correct behavior of S3 operations such as upload,
download, list, and delete without making real AWS S3 calls.
"""

import pytest
from unittest.mock import patch, MagicMock
from botocore.exceptions import NoCredentialsError, ClientError
from infrastructure.aws.s3.s3_manager import S3Manager


# ------------- UPLOAD ----------------

@patch("infrastructure.aws.s3.s3_manager.boto3.client")
@patch("infrastructure.aws.s3.s3_manager.get_s3_config")
def test_upload_success(mock_config, mock_boto):
    """
    Test successful upload of a file to S3.

    Mocks the boto3 client and verifies that the upload_file method is called
    with the expected parameters.
    """
    mock_config.return_value = {
        "bucket": "test-bucket",
        "access_key": "AKIA...",
        "secret_key": "SECRET",
        "region": "eu-west-3"
    }
    mock_client = MagicMock()
    mock_boto.return_value = mock_client

    s3 = S3Manager()
    s3.upload("local.txt", "s3/path.txt")

    mock_client.upload_file.assert_called_with("local.txt", "test-bucket", "s3/path.txt")


@patch("infrastructure.aws.s3.s3_manager.boto3.client")
@patch("infrastructure.aws.s3.s3_manager.get_s3_config")
def test_upload_file_not_found(mock_config, mock_boto):
    """
    Test error handling when the local file to upload is not found.

    Simulates a FileNotFoundError and ensures that no unhandled exception is raised.
    """
    mock_config.return_value = {
        "bucket": "test-bucket",
        "access_key": "AKIA...",
        "secret_key": "SECRET",
        "region": "eu-west-3"
    }
    mock_client = MagicMock()
    mock_client.upload_file.side_effect = FileNotFoundError()
    mock_boto.return_value = mock_client

    s3 = S3Manager()
    s3.upload("nonexistent.txt", "s3/missing.txt")


# ------------- DOWNLOAD ----------------

@patch("infrastructure.aws.s3.s3_manager.boto3.client")
@patch("infrastructure.aws.s3.s3_manager.get_s3_config")
def test_download_success(mock_config, mock_boto):
    """
    Test successful download of a file from S3.

    Verifies that the correct bucket, key, and local path are used.
    """
    mock_config.return_value = {
        "bucket": "test-bucket",
        "access_key": "AKIA...",
        "secret_key": "SECRET",
        "region": "eu-west-3"
    }
    mock_client = MagicMock()
    mock_boto.return_value = mock_client

    s3 = S3Manager()
    s3.download("s3/file.txt", "local_file.txt")

    mock_client.download_file.assert_called_with("test-bucket", "s3/file.txt", "local_file.txt")


@patch("infrastructure.aws.s3.s3_manager.boto3.client")
@patch("infrastructure.aws.s3.s3_manager.get_s3_config")
def test_download_client_error(mock_config, mock_boto):
    """
    Test download when a ClientError is raised (e.g. file not found in S3).

    Ensures error is handled gracefully and the correct error message is printed.
    """
    mock_config.return_value = {
        "bucket": "test-bucket",
        "access_key": "AKIA...",
        "secret_key": "SECRET",
        "region": "eu-west-3"
    }
    mock_client = MagicMock()
    mock_client.download_file.side_effect = ClientError(
        error_response={"Error": {"Code": "404", "Message": "Not Found"}},
        operation_name="DownloadFile"
    )
    mock_boto.return_value = mock_client

    s3 = S3Manager()
    s3.download("s3/missing.txt", "local_file.txt")


# ------------- LIST ----------------

@patch("infrastructure.aws.s3.s3_manager.boto3.client")
@patch("infrastructure.aws.s3.s3_manager.get_s3_config")
def test_list_objects(mock_config, mock_boto):
    """
    Test listing files in an S3 bucket under a specific prefix.

    Mocks a successful response with 2 files and checks that they are returned.
    """
    mock_config.return_value = {
        "bucket": "test-bucket",
        "access_key": "AKIA...",
        "secret_key": "SECRET",
        "region": "eu-west-3"
    }
    mock_client = MagicMock()
    mock_client.list_objects_v2.return_value = {
        "Contents": [{"Key": "file1.txt"}, {"Key": "file2.txt"}]
    }
    mock_boto.return_value = mock_client

    s3 = S3Manager()
    files = s3.list("")

    assert files == ["file1.txt", "file2.txt"]


# ------------- DELETE ----------------

@patch("infrastructure.aws.s3.s3_manager.boto3.client")
@patch("infrastructure.aws.s3.s3_manager.get_s3_config")
def test_delete_success(mock_config, mock_boto):
    """
    Test deletion of a file from S3.

    Verifies that the delete_object method is called with the correct bucket and key.
    """
    mock_config.return_value = {
        "bucket": "test-bucket",
        "access_key": "AKIA...",
        "secret_key": "SECRET",
        "region": "eu-west-3"
    }
    mock_client = MagicMock()
    mock_boto.return_value = mock_client

    s3 = S3Manager()
    s3.delete("to_delete.txt")

    mock_client.delete_object.assert_called_with(Bucket="test-bucket", Key="to_delete.txt")
