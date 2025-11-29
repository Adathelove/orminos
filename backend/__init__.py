"""
Backend abstraction layer for registry storage.

Currently provides the RegistryBackend protocol; concrete implementations
(e.g. JSON-backed, day-directory-backed) live in separate modules.
"""

from .db_backend import RegistryBackend

__all__ = ["RegistryBackend"]
