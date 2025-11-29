from __future__ import annotations

from pathlib import Path

from .db_backend import RegistryBackend
from .registry_ops_adapter import RegistryOpsJsonAdapter


def get_active_backend() -> RegistryBackend:
    """
    The global backend selection point.

    Currently returns a compatibility adapter for the existing
    registry_ops JSON behavior. This preserves all current behavior.

    Later steps will replace this with a config-based or dynamic
    backend selector without touching call sites.
    """
    return RegistryOpsJsonAdapter()
