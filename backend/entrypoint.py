from __future__ import annotations

from pathlib import Path

from .db_backend import RegistryBackend
from .registry_ops_adapter import RegistryOpsJsonAdapter


from .meta import DAY_DIR_MODE
from .daydir_backend import DayDirectoryBackend
from .registry_ops_adapter import RegistryOpsJsonAdapter

def get_active_backend():
    if DAY_DIR_MODE:
        return DayDirectoryBackend(Path("registry"))
    return RegistryOpsJsonAdapter()
