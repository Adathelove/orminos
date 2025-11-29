# cli_parser.py

from docopt import docopt

DOC = """
Usage:
  registry.py --url=<u>
  registry.py --today
  registry.py --auto
  registry.py --today --select

Options:
  -u --url=<u>     URL to register
  --today          Show all entries for today
  --auto          Use active browser tab URL (macOS Safari)
  --select         Select one of today's entries interactively
"""

def parse_args():
    return docopt(DOC)
