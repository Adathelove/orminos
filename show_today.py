# show_today.py

from today_core import get_today_entries
from today_output import print_today_entries

def show_today():
    entries = get_today_entries()
    print_today_entries(entries)
