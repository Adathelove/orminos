from db import load_db

def find_persona_by_date(persona: str, date_str: str):
    """
    Return all entries for a given persona on a specific date.
    No hardcoded persona names.
    """
    db = load_db()
    matches = []

    for entry in db.values():
        if entry.get("persona") == persona and entry.get("date") == date_str:
            matches.append(entry)

    return matches
