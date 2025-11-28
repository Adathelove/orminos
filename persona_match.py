# persona_match.py

# Step 1: keep the static dict exactly as-is
# We only wrap it in a function. No behavior changes.

def load_known_personas():
    return {
        "keyboard": ["keyboard", "km", "maestro"],
        "chaos": ["chaos"],
        "orminos": ["orminos"],
        "techne": ["techne"],
        "hephaiste": ["hephaiste"],
        # Extend as needed
    }


def match_persona(url: str):
    personas = load_known_personas()
    url_lower = url.lower()

    for persona, patterns in personas.items():
        for p in patterns:
            if p in url_lower:
                return persona

    return None
