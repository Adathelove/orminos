from __future__ import annotations

import json
from pathlib import Path
from typing import Any, MutableMapping

from .db_backend import RegistryBackend


class JsonBackend(RegistryBackend):
    """
    Thin wrapper around the current JSON file storage.

    This preserves existing behavior entirely. It merely exposes the same
    load/save logic through the RegistryBackend interface so we can later
    substitute implementations without touching registry_ops.
    """

    def __init__(self, path: Path):
        self.path = path

    def load(self) -> MutableMapping[str, Any]:
        if not self.path.exists():
            return {}
        with self.path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, data: MutableMapping[str, Any]) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
