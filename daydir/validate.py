# daydir/validate.py

from __future__ import annotations
import os
from pathlib import Path
from logger import warn, fail

# ----------------------------------------
# validate_storage_root
# ----------------------------------------

def validate_storage_root(root: str | Path):
    """
    Validate the configured storage_root.

    Rules:
      - must not be empty
      - must be a directory that exists
      - must not contain traversal ('..')
      - may be relative or absolute (no requirement either way)
    Returns:
      Path(root) on success
      None on failure
    """

    if not root:
        fail("storage_root invalid: empty value.")
        return None

    p = Path(root)

    # Reject traversal segments
    if ".." in p.parts:
        fail(f"storage_root invalid: contains traversal sequences: {root}")
        return None

    # Must exist and be a directory
    if not p.exists():
        fail(f"storage_root does not exist: {root}")
        return None
    if not p.is_dir():
        fail(f"storage_root exists but is not a directory: {root}")
        return None

    return p


# ----------------------------------------
# validate_daydir_name
# ----------------------------------------

def validate_daydir_name(name: str):
    """
    Validate the day-directory name.

    Rules:
      - nonempty
      - no slashes
      - no traversal
      - basic sanity check for format: YYYY-MM-DD-EEE
        (soft check; does not enforce full date correctness)

    Returns:
      name on success
      None on failure
    """

    if not name or not isinstance(name, str):
        fail("daydir name invalid: empty or non-string.")
        return None

    # Reject path separators
    if "/" in name or "\\" in name:
        fail(f"daydir name invalid: contains path separators: {name}")
        return None

    # Reject traversal
    if ".." in name.split(os.sep):
        fail(f"daydir name invalid: contains traversal: {name}")
        return None

    # Basic structure check (loose pattern)
    parts = name.split("-")
    if len(parts) != 4:
        warn(f"daydir name unusual format (expected YYYY-MM-DD-EEE): {name}")

    return name


# ----------------------------------------
# validate_daydir_path
# ----------------------------------------

def validate_daydir_path(root: str | Path, dirname: str):
    """
    Validate storage_root + daydir-name combination.

    Returns:
      Path(root/dirname) if both components are valid
      None on failure
    """

    root_p = validate_storage_root(root)
    if root_p is None:
        return None

    dirname_s = validate_daydir_name(dirname)
    if dirname_s is None:
        return None

    full = root_p / dirname_s

    # Ensure no traversal after join
    # (normalize and ensure root_p is still the anchor)
    try:
        resolved_full = full.resolve(strict=False)
        resolved_root = root_p.resolve(strict=False)

        if resolved_root not in resolved_full.parents and resolved_full != resolved_root:
            fail(f"daydir path escapes storage_root: {full}")
            return None

    except Exception:
        fail(f"daydir path resolution error: {full}")
        return None

    return resolved_full
