from datetime import datetime

def icu_date():
    # Format: EEE MMM d
    # Python approximation: %a %b %-d
    # (macOS supports %-d for no leading zero)
    return datetime.now().strftime("%a %b %-d")
