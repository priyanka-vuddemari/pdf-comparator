# json_loader.py

import json

def load_json(json_path: str) -> dict:
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return {}
