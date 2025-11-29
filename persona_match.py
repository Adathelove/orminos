# persona_match.py

import os
from persona_normalize import normalize

PHYLE_PATH = os.path.join(os.path.dirname(__file__), "Phyle.txt")


def load_known_personas():
    """
    Step 2:
    Load persona names directly from Phyle.txt, with NO normalization.
    This will cause matching to fail, as planned.
    """
    personas = {}

    if not os.path.exists(PHYLE_PATH):
        return {}

    with open(PHYLE_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            persona_key = line            # keep original key (emoji + name)
            p_norm = normalize(line)      # normalized search pattern
            personas[persona_key] = [p_norm]

    return personas


def match_persona(url: str):
    personas = load_known_personas()
    url_norm = normalize(url)

    for persona, patterns in personas.items():
        for p in patterns:
            if p in url_norm:
                return persona

    return None
