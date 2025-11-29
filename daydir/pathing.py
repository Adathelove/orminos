# daydir/pathing.py

import os
from settings import load_settings
from logger import warn, abort, info

from .naming import day_directory_name
from .validate import validate_daydir_path


def compute_daydir_path():
    """
    Compute the validated absolute day-directory path.

    Override precedence:
      1. DAYDIR_OVERRIDE_ROOT environment variable (if set)
      2. settings.storage_root (if override not set)
    """

    # --------------------------------------------
    # 1. Override bypasses settings entirely
    # --------------------------------------------
    override = os.environ.get("DAYDIR_OVERRIDE_ROOT")
    if override:
        root = override
        dirname = day_directory_name()

        validated = validate_daydir_path(root, dirname)
        if validated is None:
            warn("Day-directory path validation failed (override root).")
            return None

        return str(validated)

    # --------------------------------------------
    # 2. Fallback: settings.json
    # --------------------------------------------
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

    return str(validated)
