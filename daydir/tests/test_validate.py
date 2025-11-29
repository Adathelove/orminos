# daydir/tests/test_validate.py

import os
from pathlib import Path
from daydir.validate import validate_storage_root

def test_validate_storage_root_basic():
    """
    Minimal smoke test:
    - create a temporary directory
    - validate it as a storage_root
    - ensure we get back a Path object
    """
    # setup: temporary directory
    tmp = Path("tmp_test_root")
    tmp.mkdir(exist_ok=True)

    try:
        result = validate_storage_root(str(tmp))
        assert isinstance(result, Path), "Expected a Path object"
        assert result == tmp, "Path should round-trip unchanged"
    finally:
        # clean up
        # Only remove if empty; ignore errors if anything is left
        try:
            tmp.rmdir()
        except OSError:
            pass

