PLAN_daydir.md

# Step Summary

Stabilize the DayDir backend into its first complete, validated, and documented form.

## Step 1

Define and finalize the DayDir schema v1, including required fields and `schema_version`.

- Review pathing.py, naming.py, and driver_daydir.py to ensure the basic code paths are correct:
    - detect and process path overrides from environment variables and command-line options
    - remove anything unnecessary for the core functionality of checking whether a directory exists
    - establish a clear, unified pattern for directory naming and JSON file placement
    - apply the schema only to actual `.json` files, not directories
    - ensure directory names and schema expectations follow a shared code path so that locating the root and its day-directories is consistent
- Use test-driven development; schema rules and validation semantics are exercised through targeted tests.
(Previous Step 2 validation requirements are now absorbed here.)

## Step 2

Implement strict override-first pathing and validation rules for root, daydir names, and allowed directory creation.

- Happy-path load test.
- File-existence validation test. (Implemented first.)
- File-name/content rule validation. (Already satisfied by current naming rules.)

## Step 3

Align DayDir backend behavior with the JSON backend to ensure identical load/save semantics and interface guarantees.
