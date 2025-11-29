# platform_utils.py

import sys

def detect_platform():
    p = sys.platform

    if p == "darwin":
        return "macos"
    if p.startswith("linux"):
        return "linux"
    if p in ("win32", "cygwin"):
        return "windows"

    return "unknown"
