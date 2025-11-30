PLAN_daydir.md

# Step Summary

Stabilize the DayDir backend into its first complete, validated, and documented form.

## Step 1

Define and finalize the DayDir schema v1, including required fields and `schema_version`.

- Use test-driven development; schema rules and validation semantics are exercised through targeted tests.
(Previous Step 2 validation requirements are now absorbed here.)

## Step 2

Implement strict override-first pathing and validation rules for root, daydir names, and allowed directory creation.

- Happy-path load test.
- File-existence validation test. (Implemented first.)
- File-name/content rule validation. (Already satisfied by current naming rules.)

## Step 3

Align DayDir backend behavior with the JSON backend to ensure identical load/save semantics and interface guarantees.
