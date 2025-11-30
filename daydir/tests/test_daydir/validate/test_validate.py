from pathlib import Path
from daydir.validate import validate_storage_root
from logger import info, fail

def test_validate_storage_root_basic():
    """
    Single test with visible logger output.
    Exercise both:
        - a valid storage_root
        - an invalid one
    """

    info("TEST: starting validate_storage_root_basic")

    # --- Valid directory scenario ---
    tmp = Path("tmp_test_root")
    tmp.mkdir(exist_ok=True)

    info(f"TEST: validating existing directory: {tmp}")
    result_valid = validate_storage_root(str(tmp))
    assert result_valid == tmp

    # --- Invalid directory scenario ---
    invalid_dir = "does_not_exist_12345"

    info(f"TEST: validating non-existent directory: {invalid_dir}")
    result_invalid = validate_storage_root(invalid_dir)
    assert result_invalid is None  # should log FAIL

    # Cleanup
    try:
        tmp.rmdir()
        info("TEST: cleanup succeeded.")
    except Exception as e:
        fail(f"TEST: cleanup failed: {e}")

    info("TEST: validate_storage_root_basic complete.")
