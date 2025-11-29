# current_url.py

import subprocess
from platform_utils import detect_platform

def get_current_url():
    """
    Return the URL of the frontmost browser tab.
    Currently implemented for macOS Safari.
    Returns None if unsupported or unavailable.
    """
    platform = detect_platform()

    if platform == "macos":
        try:
            result = subprocess.run(
                [
                    "osascript",
                    "-e",
                    'tell application "Safari" to return URL of front document'
                ],
                capture_output=True,
                text=True,
            )
            url = result.stdout.strip()
            return url if url else None
        except Exception:
            return None

    # Linux/Windows unresolved for now
    return None
