#!/usr/bin/env python

from __future__ import annotations

import sys
import os
from docopt import docopt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from logger import info, fail
from registry_ops.registry_ops import register_url  # placeholder import

USAGE = """
RegistryOps Utility

Usage:
  ./driver_registry --noop
  ./driver_registry (-h | --help)

Options:
  --noop     Perform a no-op placeholder action
  -h --help  Show this screen.
"""

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    args = docopt(USAGE, argv=argv)

    do_noop = args.get("--noop")

    if do_noop:
        info("registry_ops driver placeholder: no-op executed")
        return 0

    fail("No action specified.")
    return -1

if __name__ == "__main__":
    sys.exit(main())

