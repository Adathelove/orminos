# cli_parser.py

from docopt import docopt

DOC = """
Persona URL Registry
Usage:
  registry.py --url=<u>

Options:
  -u --url=<u>   URL to register
"""

def parse_args():
    return docopt(DOC)
