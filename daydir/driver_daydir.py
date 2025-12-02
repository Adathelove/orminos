#!/usr/bin/env python

from __future__ import annotations

import sys
import os
from docopt import docopt

# ---------------------------------------------------------
# Path injection must happen BEFORE importing logger
# ---------------------------------------------------------
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from logger import info, warn, fail, success
from daydir.DayDir import DayDir, DayDirError   # <-- FIXED

USAGE = """
DayDir Utility

Usage:
  ./driver_daydir --file=FILE [--init | --createNewDay]
  ./driver_daydir (-h | --help)

Options:
  --file=FILE       JSON settings file
  --init            Discover existing day directories
  --createNewDay    Create a new day directory for today
  -h --help         Show this screen.
"""

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    args = docopt(USAGE, argv=argv)

    settings_file = args.get("--file")
    if not settings_file:
        fail("Missing required --file")
        return -1

    do_init = args.get("--init")
    do_create = args.get("--createNewDay")

    # ---------------------------------------------------------
    # DayDir construction (clean failure, no stack trace)
    # ---------------------------------------------------------
    try:
        dd = DayDir(settings_file)
    except DayDirError as e:
        fail(f"DayDir construction failed: {e}")
        return -1   # <-- clean exit, no traceback

    info(f"Settings file read: {os.path.abspath(settings_file)}")
    info(dd.settings.return_settings_as_json())
    if do_init:
        dd.init()
    if do_create:
        dd.createNewDay()
    info("DayDir constructed successfully.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
