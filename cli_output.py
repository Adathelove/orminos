# cli_output.py

import json

def print_registration_result(entry, existed: bool):
    if existed:
        print("URL already registered:")
    else:
        print("Registered:")

    # Show real UTF-8 emoji instead of \\uXXXX
    print(json.dumps(entry, indent=2, ensure_ascii=False))
