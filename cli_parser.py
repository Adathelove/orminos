# cli_parser.py

from docopt import docopt

DOC = """
Usage:
  registry.py --url=<u>
  registry.py --today

Options:
  -u --url=<u>     URL to register
  --today          Show all entries for today
"""

def parse_args():
    return docopt(DOC)
