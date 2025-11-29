# today_core.py

from db import load_db
from date_utils import icu_date

def get_today_entries():
    """
    Returns a list of tuples:
        (url, persona, version)
    Pure function: no printing, no questionary, no side effects.
    """
    db = load_db()
    today = icu_date()

    return [
        (url, e["persona"], e["version"])
        for url, e in db.items()
        if e.get("date") == today
    ]
