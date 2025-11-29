import os
from .normalize import normalize

PHYLE_PATH = os.path.join(os.path.dirname(__file__), "..", "Phyle.txt")

def load_known_personas():
    personas = {}

    if not os.path.exists(PHYLE_PATH):
        return {}

    with open(PHYLE_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            persona_key = line
            p_norm = normalize(line)
            personas[persona_key] = [p_norm]

    return personas
