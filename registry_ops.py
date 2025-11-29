# registry_ops.py

import json
from db import load_db, save_db
from persona import match_persona
from versioning import resolve_version
from date_utils import icu_date
from persona.resolve import resolve_persona_from_url
from collision_check import check_same_day_persona
from db_queries import find_persona_by_date
from open_link import open_link
# Backend pivot (inactive). Future wiring point.
from backend.entrypoint import get_active_backend  # noqa: F401

def load_registry():
    """
    Load registry data.
    Now routed through the backend adapter (read-only A3.6).
    """
    backend = get_active_backend()
    return backend.load()

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

    # PRE-SAVE COLLISION CHECK
    # Determine if adding this entry would cause a same-day collision
    existing_matches = find_persona_by_date(persona, date_str)
    will_collide = len(existing_matches) >= 1

    if will_collide:
        open_link(url)
        resp = input("Same-day entry detected. Confirm registration? (y/N): ").strip().lower()
        if resp != "y":
            return entry, True  # treat as not saved

    db[url] = entry
    save_db(db)

    # persona-aware collision check
    check_same_day_persona(persona, url)

    return entry, False
