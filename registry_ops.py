# registry_ops.py

import json
from db import load_db, save_db
from persona_match import match_persona
from versioning import resolve_version
from date_utils import icu_date
from resolve_persona import resolve_persona_from_url

def register_url(url: str):
    """
    Pure operation for registering a URL.
    Encapsulates all steps but makes no behavioral changes.
    """
    db = load_db()

    # Existing?
    if url in db:
        return db[url], True  # (entry, already_exists)

    persona = resolve_persona_from_url(url)

    # Resolve version
    version = resolve_version(db, persona)

    # Assign date
    date_str = icu_date()

    # Register
    entry = {
        "persona": persona,
        "version": version,
        "date": date_str
    }

    db[url] = entry
    save_db(db)

    return entry, False
