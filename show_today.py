# show_today.py

from db import load_db
from date_utils import icu_date

def show_today():
    db = load_db()
    today = icu_date()

    records = [
        (url, e["persona"], e["version"])
        for url, e in db.items()
        if e.get("date") == today
    ]

    if not records:
        print("No entries for today.")
        return

    for url, persona, version in records:
        print(f"{persona} v{version} — {url}")
