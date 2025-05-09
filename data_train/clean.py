import os
import json

# Base path = dossier du script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_PATH = os.path.join(BASE_DIR, "fine_tune_dataset.jsonl")
OUTPUT_PATH = os.path.join(BASE_DIR, "fine_tune_dataset_clean.jsonl")

with open(INPUT_PATH, "r", encoding="utf-8") as f_in, open(OUTPUT_PATH, "w", encoding="utf-8") as f_out:
    for line in f_in:
        try:
            json_obj = json.loads(line)
            json.dump(json_obj, f_out, ensure_ascii=False)
            f_out.write("\n")
        except json.JSONDecodeError:
            print("Ligne ignorée (invalide) :", line.strip())