# open_link.py

import subprocess
from platform_utils import detect_platform


def open_link(target: str):
    """
    Abstract 'open a link or file' action.
    macOS:    open <target>
    Linux:    xdg-open <target>
    Windows:  start <target> (shell=True)
    """
    platform = detect_platform()

    if platform == "macos":
        subprocess.run(["open", target])
    elif platform == "linux":
        subprocess.run(["xdg-open", target])
    elif platform == "windows":
        subprocess.run(["start", target], shell=True)
    else:
        raise RuntimeError(f"Unsupported platform: {platform}")
