from .match import match_persona

def resolve_persona_from_url(url: str):
    persona = match_persona(url)
    if persona is None:
        persona = input("Unknown persona. Enter persona name: ").strip()
    return persona
