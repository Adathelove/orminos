#!/usr/bin/env python

"""
Persona URL Registry
Usage:
  registry.py --url=<u>

Options:
  -u --url=<u>   URL to register
"""

import json
import os
from datetime import datetime
from docopt import docopt

# --- New import replacing inline DB functions ---
from db import load_db, save_db
from date_utils import icu_date


# ---------------------------
# Persona Matching Scaffold
# ---------------------------
KNOWN_PERSONAS = {
    "keyboard": ["keyboard", "km", "maestro"],
    "chaos": ["chaos"],
    "orminos": ["orminos"],
    "techne": ["techne"],
    "hephaiste": ["hephaiste"],
    # Extend as needed
}


def match_persona(url: str):
    url_lower = url.lower()
    for persona, patterns in KNOWN_PERSONAS.items():
        for p in patterns:
            if p in url_lower:
                return persona
    return None  # unresolved → manual confirmation required


# ---------------------------
# Version Resolver
# ---------------------------
def resolve_version(existing_entries, persona):
    # Extract existing versions for this persona on this date
    versions = [
        entry["version"]
        for entry in existing_entries.values()
        if entry["persona"] == persona
    ]
    if not versions:
        return 1
    return max(versions) + 1


# ---------------------------
# Main
# ---------------------------
def main():
    args = docopt(__doc__)
    url = args["--url"]

    db = load_db()

    # Existing?
    if url in db:
        print("URL already registered:")
        print(json.dumps(db[url], indent=2))
        return

    # Resolve persona
    persona = match_persona(url)
    if persona is None:
        persona = input("Unknown persona. Enter persona name: ").strip()

    # Resolve version
    version = resolve_version(db, persona)

    # Assign date
    date_str = icu_date()

    # Register
    db[url] = {
        "persona": persona,
        "version": version,
        "date": date_str
    }

    save_db(db)

    print("Registered:")
    print(json.dumps(db[url], indent=2))


if __name__ == "__main__":
    main()
