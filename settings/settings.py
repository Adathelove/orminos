import os
import json

from logger import info, warn, fail, abort, exception
from .defaults import DEFAULT_SETTINGS_PATH


def settings_path():
    """
    Returns the configured settings path.
    For A4.0, this is always DEFAULT_SETTINGS_PATH.
    """
    return DEFAULT_SETTINGS_PATH


def load_settings():
    """
    Load settings.json if valid.
    If anything is wrong, log and return None.
    """
    path = settings_path()

    # 1. Directory exists?
    dir_path = os.path.dirname(path)
    if not os.path.isdir(dir_path):
        abort(f"Settings directory does not exist: {dir_path}")
        return None

    # 2. File exists?
    if not os.path.isfile(path):
        abort(f"Settings file missing: {path}")
        return None

    # 3. File readable?
    if not os.access(path, os.R_OK):
        fail(f"Settings file exists but is not readable: {path}")
        return None

    # 4. Attempt to load JSON
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        fail(f"Settings file contains invalid JSON: {path}")
        return None
    except Exception as e:
        exception(f"Unexpected error reading settings: {e}")
        return None


def ensure_settings():
    """
    Future extension point.
    For A4.0:
        - Attempt to load settings.
        - Return dict or None.
    No creation or fallback yet.
    """
    return load_settings()
