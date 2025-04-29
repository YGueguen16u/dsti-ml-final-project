# back_end/models/nlp/model_training.py

from .s3_nlp_controller import S3NLPController

if __name__ == "__main__":
    controller = S3NLPController()

    # Upload example
    controller.upload(
        local_path="data/nlp/fine_tune_dataset.jsonl",
        s3_key="nlp/datasets/fine_tune_dataset.jsonl"
    )

    # Download example
    controller.download(
        s3_key="nlp/outputs/prediction_2025-04-10.json",
        local_path="data/local_prediction.json"
    )

    # List files
    controller.list_files("nlp/datasets/")
