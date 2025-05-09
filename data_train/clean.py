import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH = os.path.join(BASE_DIR, "fine_tune_dataset.jsonl")
OUTPUT_PATH = os.path.join(BASE_DIR, "fine_tune_dataset_clean.jsonl")

def force_content_to_str(messages):
    for msg in messages:
        if isinstance(msg["content"], dict):
            msg["content"] = json.dumps(msg["content"], ensure_ascii=False)
    return messages

with open(INPUT_PATH, "r", encoding="utf-8") as f_in, open(OUTPUT_PATH, "w", encoding="utf-8") as f_out:
    for line in f_in:
        try:
            obj = json.loads(line)
            obj["messages"] = force_content_to_str(obj["messages"])
            json.dump(obj, f_out, ensure_ascii=False)
            f_out.write("\n")
        except json.JSONDecodeError:
            print("Ligne ignorée (invalide) :", line.strip())