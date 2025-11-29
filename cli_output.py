# cli_output.py

import json

def print_registration_result(entry, existed: bool):
    if existed:
        print("URL already registered:")
    else:
        print("Registered:")

    print(json.dumps(entry, indent=2))
