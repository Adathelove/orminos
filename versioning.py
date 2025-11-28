# versioning.py

def resolve_version(existing_entries, persona):
    """
    Extract version number for persona within the registry.
    Pure function. No side effects.
    """
    versions = [
        entry["version"]
        for entry in existing_entries.values()
        if entry["persona"] == persona
    ]

    if not versions:
        return 1

    return max(versions) + 1
