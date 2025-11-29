# today_picker.py

from today_core import get_today_entries
from open_link import open_link

def pick_today_entry():
    import questionary

    entries = get_today_entries()

    if not entries:
        print("No entries for today.")
        return

    # Format entries for user display
    formatted = [
        f"{persona} v{version} — {url}"
        for url, persona, version in entries
    ]

    choice = questionary.select(
        "Select entry to open:",
        choices=formatted
    ).ask()

    if not choice:
        return

    # Split `persona vX — URL`
    _, url = choice.split("—", 1)
    open_link(url.strip())
