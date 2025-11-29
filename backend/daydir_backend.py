from __future__ import annotations

from pathlib import Path
from .db_backend import RegistryBackend

class DayDirectoryBackend(RegistryBackend):
    def __init__(self, root: Path):
        self.root = root

    def load(self):
        return {}  # placeholder

    def save(self, data):
        pass       # placeholder
