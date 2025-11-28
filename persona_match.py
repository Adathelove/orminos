# persona_match.py

import os

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

            # raw line: e.g. "🔩 Orminos"
            persona_key = line  # unnormalized
            personas[persona_key] = [line]  # patterns list

    return personas


def match_persona(url: str):
    personas = load_known_personas()
    url_lower = url.lower()

    for persona, patterns in personas.items():
        for p in patterns:
            # still raw
            if p.lower() in url_lower:
                return persona

    return None
