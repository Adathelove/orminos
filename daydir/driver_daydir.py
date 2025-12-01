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
  daydir --root=DIR
  daydir (-h | --help)

Options:
  --root=DIR    Root directory for DayDir
  -h --help     Show this screen.
"""

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    args = docopt(USAGE, argv=argv)

    root = args.get("--root")
    if not root:
        fail("Missing required --root")
        return -1

    # ---------------------------------------------------------
    # DayDir construction (clean failure, no stack trace)
    # ---------------------------------------------------------
    try:
        dd = DayDir(root)
    except DayDirError as e:
        fail(f"DayDir construction failed: {e}")
        return -1   # <-- clean exit, no traceback

    info("DayDir constructed successfully.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
