from __future__ import annotations

import os
import json
from pathlib import Path

from .db_backend import RegistryBackend
from logger import warn, fail, exception, info
from daydir.pathing import compute_daydir_path

class DayDirectoryBackend(RegistryBackend):
    def __init__(self, root: Path):
        # root is still kept for future wiring,
        # but compute_daydir_path() determines actual path.
        self.root = root

    def load(self):
        """
        A4.2:
        - Resolve daydir path.
        - If settings invalid → {}.
        - If directory or file missing → {}.
        - Else read JSON safely.
        """
        daydir = compute_daydir_path()
        if daydir is None:
            warn("DayDirectoryBackend.load: cannot compute day-directory path.")
            return {}

        if not os.path.isdir(daydir):
            # Not an error; simply no registry for today yet.
            return {}

        json_path = os.path.join(daydir, "registry.json")

        if not os.path.isfile(json_path):
            # Directory exists but registry.json does not.
            return {}

        # Attempt read
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            fail(f"Invalid JSON in {json_path}")
            return {}
        except Exception as e:
            exception(f"Unexpected error reading {json_path}: {e}")
            return {}

    def save(self, data):
        """
        A4.3:
        - Resolve daydir path.
        - Ensure directory exists.
        - Write registry.json atomically.
        """
        daydir = compute_daydir_path()
        if daydir is None:
            warn("DayDirectoryBackend.save: cannot compute day-directory path.")
            return

        # Ensure the day-directory exists (but not parents beyond storage_root).
        try:
            if not os.path.isdir(daydir):
                os.makedirs(daydir, exist_ok=True)
        except Exception as e:
            exception(f"Failed to create day-directory {daydir}: {e}")
            return

        json_path = os.path.join(daydir, "registry.json")

        # Attempt write
        try:
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            exception(f"Failed to write {json_path}: {e}")
            return

