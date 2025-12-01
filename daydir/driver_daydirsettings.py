#!/usr/bin/env python

from __future__ import annotations

import sys
import os
import json
from docopt import docopt

from DayDirSettings import DayDirSettings, DayDirSettingsException

# ---------------------------------------------------------
# Path injection must happen BEFORE importing logger
# ---------------------------------------------------------
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from logger import info, warn, fail, success

USAGE = """
DayDir Settings Utility

Usage:
  daydir/driver_daydirsettings.py --file=FILE
  daydir/driver_daydirsettings.py -f FILE
  daydir/driver_daydirsettings.py (-h | --help)

Options:
  -f FILE --file=FILE   JSON settings file
  -h --help             Show this screen.
"""

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    args = docopt(USAGE, argv=argv)

    settings_file = args.get("--file")
    if not settings_file:
        fail("Missing required --file")
        return -1

    try:
        s = DayDirSettings(settings_file)
    except DayDirSettingsException as e:
        fail(f"Settings load failed: {e}")
        return -1

    info("Settings loaded successfully.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
