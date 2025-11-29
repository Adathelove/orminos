# resolve_persona.py

from persona import match_persona

def resolve_persona_from_url(url: str):
    """
    Wrap persona resolution + fallback prompt.
    No behavioral changes.
    """
    persona = match_persona(url)

    if persona is None:
        persona = input("Unknown persona. Enter persona name: ").strip()

    return persona
