from __future__ import annotations

from pathlib import Path
from typing import Any, MutableMapping

# Import existing behavior — unchanged
import registry_ops                     # current registry logic

from .db_backend import RegistryBackend


class RegistryOpsJsonAdapter(RegistryBackend):
    """
    Adapter that preserves the current registry_ops.py JSON behavior.
    This allows backend wiring without altering registry_ops itself.
    """

    def __init__(self) -> None:
        # registry_ops already defines the JSON file path internally
        # so we do not store or override anything here.
        pass

    def load(self) -> MutableMapping[str, Any]:
        # Direct passthrough to existing implementation.
        return registry_ops.load_registry()

    def save(self, data: MutableMapping[str, Any]) -> None:
        # Direct passthrough to existing implementation.
        registry_ops.save_registry(data)
