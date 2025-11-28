# persona_match.py

import os

PHYLE_PATH = os.path.join(os.path.dirname(__file__), "Phyle.txt")

def load_known_personas():
    """
    Step 2:
    Load persona names directly from Phyle.txt, no normalization.
    This will mostly break matching, as planned.
    """
    personas = {}

    if not os.path.exists(PHYLE_PATH):
        # safety fallback (won't help matching, but avoids crashes)
        return {}

    with open(PHYLE_PATH", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Example: "🔩 Orminos"
            # We keep this whole line as a key → guaranteed mismatch
            persona_key = line  # ← raw, unnormalized

            # Patterns list includes the raw line only
            personas[persona_key] = [line]

    return personas


def match_persona(url: str):
    personas = load_known_personas()
    url_lower = url.lower()

    for persona, patterns in personas.items():
        for p in patterns:
            if p.lower() in url_lower:  # matching against raw names
                return persona

    return None
