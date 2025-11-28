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
from registry_ops import register_url

def main():
    args = parse_args()
    url = args["--url"]

    entry, existed = register_url(url)

    if existed:
        print("URL already registered:")
    else:
        print("Registered:")

    print(json.dumps(entry, indent=2))

if __name__ == "__main__":
    main()
