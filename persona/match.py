from .normalize import normalize
from .phyle_loader import load_known_personas

def match_persona(url: str):
    personas = load_known_personas()
    url_norm = normalize(url)

    for persona, patterns in personas.items():
        for p in patterns:
            if p in url_norm:
                return persona

    return None
