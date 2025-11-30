#!/usr/bin/env python

# daydir/driver.py
from __future__ import annotations

import sys
import os
import json
from pathlib import Path

# -----------------------------------------------------------------------------
# Hack: allow this internal submodule to reach the top-level logger package.
# This mirrors the pytest conftest path injection strategy.
# -----------------------------------------------------------------------------
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from logger import info, warn, fail, success, abort    # noqa: E402
from docopt import docopt                              # noqa: E402

from daydir.pathing import compute_daydir_path         # noqa: E402
from daydir.naming import day_directory_name           # noqa: E402


USAGE = """
DayDir Utility (internal module driver)

Usage:
  daydir path [--root=DIR]
  daydir inspect [--root=DIR]
  daydir mkdir [--root=DIR]
  daydir init [--root=DIR]
  daydir schema [--root=DIR]
  daydir (-h | --help)

Options:
  --root=DIR     Override DAYDIR_OVERRIDE_ROOT
  -h --help      Show this screen.
"""


# -----------------------------------------------------------------------------
# Commands
# -----------------------------------------------------------------------------

def cmd_path():
    """Print validated day-directory path."""
    path = compute_daydir_path()
    if path is None:
        fail("Unable to compute day-directory path.")
        return
    info(f"Day-directory path: {path}")


def cmd_inspect():
    """List contents of the day-directory (if present)."""
    path = compute_daydir_path()
    if path is None:
        fail("Path invalid.")
        return

    p = Path(path)
    if not p.exists():
        warn(f"Day-directory does not exist: {path}")
        return

    info(f"Contents of {path}:")
    for item in sorted(p.iterdir(), key=lambda x: x.name):
        info(f"  {item.name}")


def cmd_mkdir():
    """Create the day-directory (one-level, no parents)."""
    path = compute_daydir_path()
    if path is None:
        fail("Path invalid.")
        return

    p = Path(path)

    if p.exists():
        warn(f"Directory already exists: {path}")
        return

    try:
        p.mkdir(parents=False, exist_ok=False)
        success(f"Created: {path}")
    except Exception as e:
        fail(f"Failed to create directory {path}: {e}")


def cmd_init():
    """
    Initialize a minimal schema v1 registry.json inside the day-directory.
    Does not import or integrate legacy registry behavior.
    """
    path = compute_daydir_path()
    if path is None:
        fail("Path invalid.")
        return

    p = Path(path)

    if not p.exists():
        try:
            p.mkdir(parents=False, exist_ok=False)
            info(f"Created directory: {path}")
        except Exception as e:
            fail(f"Failed to create directory: {e}")
            return

    registry_path = p / "registry.json"

    if registry_path.exists():
        warn(f"registry.json already exists: {registry_path}")
        return

    obj = {
        "meta": {
            "schema_version": 1,
            "generated_at": "",
            "day": day_directory_name(),
        },
        "entries": []
    }

    try:
        with registry_path.open("w", encoding="utf-8") as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)
        success(f"Initialized registry.json at: {registry_path}")
    except Exception as e:
        fail(f"Failed to write registry.json: {e}")


def cmd_schema():
    """
    Print static schema.json in this module, if present.
    """
    here = Path(__file__).parent
    schema_file = here / "schema.json"

    if not schema_file.exists():
        fail("No schema.json found in daydir package.")
        return

    try:
        text = schema_file.read_text(encoding="utf-8")
        info(text)
    except Exception as e:
        fail(f"Failed to read schema.json: {e}")


# -----------------------------------------------------------------------------
# Entry Point
# -----------------------------------------------------------------------------

def main(argv=None):

    info("daydir.driver: start")

    # ---------------------------------------------------------
    # Check override
    # ---------------------------------------------------------
    override = os.environ.get("DAYDIR_OVERRIDE_ROOT")
    if override:
        info(f"driver: override root active → {override}")
    else:
        abort("driver: DAYDIR_OVERRIDE_ROOT not set — aborting")
        return

    # Continue normal operation
    if argv is None:
        argv = sys.argv[1:]

    try:
        args = docopt(USAGE, argv=argv, help=False)
    except SystemExit:
        # docopt already printed error
        return

    # explicit usage/help flags
    if args.get("--help") or args.get("--usage"):
        print(USAGE)
        return

    if args.get("path"):
        return cmd_path()
    if args.get("inspect"):
        return cmd_inspect()
    if args.get("mkdir"):
        return cmd_mkdir()
    if args.get("init"):
        return cmd_init()
    if args.get("schema"):
        return cmd_schema()

    print(USAGE)

if __name__ == "__main__":
    main()

