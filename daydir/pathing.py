# daydir/pathing.py

import os
from settings import load_settings
from logger import warn, abort, info

from .naming import day_directory_name
from .validate import validate_daydir_path


def compute_daydir_path():
    """
    Compute the validated absolute day-directory path.

    Updated (A4.4):
      - integrate validate_daydir_path
      - return resolved Path or None
      - no creation or I/O
    """
    cfg = load_settings()
    if cfg is None:
        warn("Settings invalid — cannot compute day-directory path.")
        return None

    root = cfg.get("storage_root")
    if not root:
        abort("Settings missing 'storage_root'.")
        return None

    dirname = day_directory_name()

    validated = validate_daydir_path(root, dirname)
    if validated is None:
        warn("Day-directory path validation failed.")
        return None

    # produce string or Path?
    # A4.4 keeps return type consistent with prior behavior (string path).
    return str(validated)
