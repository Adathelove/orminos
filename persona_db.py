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
from persona_match import match_persona
from versioning import resolve_version
from cli_parser import parse_args

# ---------------------------
# Main
# ---------------------------
def main():
    args = parse_args()

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
