# persona_normalize.py
import re

def normalize(s: str):
    cleaned = re.sub(r"[^\w\s-]", "", s)
    return cleaned.strip().lower()
