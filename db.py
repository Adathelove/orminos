import json
import os

DB_PATH = os.path.expanduser("~/persona_registry.json")

def load_db():
    """
    Load the persona registry database.
    Robust against:
    - missing file
    - empty file
    - malformed JSON
    """
    # If the file does not exist → empty DB
    if not os.path.exists(DB_PATH):
        return {}

    try:
        with open(DB_PATH, "r", encoding="utf-8") as f:
            content = f.read().strip()

            # Empty file → empty DB
            if not content:
                return {}

            # Try to parse JSON
            return json.loads(content)

    except Exception:
        # Any read/parse error → empty DB
        return {}

def save_db(db):
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
