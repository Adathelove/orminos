import os
from settings import load_settings
from logger import warn, abort, info

from .naming import day_directory_name


def compute_daydir_path():
    """
    Compute the *intended* absolute path for today's day-directory.

    Rules for A4.1:
    - If settings invalid → return None.
    - No directory creation yet.
    - No read/write yet.
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
    return os.path.join(root, dirname)

