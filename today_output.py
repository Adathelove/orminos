# today_output.py

def print_today_entries(entries):
    """
    Print the entries returned by get_today_entries().
    """
    if not entries:
        print("No entries for today.")
        return

    for url, persona, version in entries:
        print(f"{persona} v{version} — {url}")
