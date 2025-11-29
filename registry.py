#!/usr/bin/env python

"""
Persona URL Registry
Usage:
  registry.py --url=<u>
  registry.py --today
  registry.py --today --select
  registry.py --auto

Options:
  -u --url=<u>        URL to register
  --today             Show all entries for today
  --select            Choose from today's entries interactively
  --auto              Use the current browser tab's URL (macOS Safari)
"""

from cli_parser import parse_args
from registry_ops import register_url
from cli_output import print_registration_result
from show_today import show_today
from today_picker import pick_today_entry
from current_url import get_current_url


def main():
    args = parse_args()

    # --- TODAY MODES ---
    if args.get("--today"):
        if args.get("--select"):
            pick_today_entry()
        else:
            show_today()
        return

    # --- AUTOMATIC URL (Safari / macOS) ---
    if args.get("--auto"):
        url = get_current_url()
        if not url:
            print("Could not get active Safari URL.")
            return
        entry, existed = register_url(url)
        print_registration_result(entry, existed)
        return

    # --- STANDARD URL MODE ---
    url = args.get("--url") or get_current_url()

    if not url:
        print("No URL provided and no active Safari URL detected.")
        return

    entry, existed = register_url(url)
    print_registration_result(entry, existed)


if __name__ == "__main__":
    main()
