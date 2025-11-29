from __future__ import annotations

from typing import Any, MutableMapping, Protocol, runtime_checkable


@runtime_checkable
class RegistryBackend(Protocol):
    """
    Abstraction for registry storage.

    The current JSON file implementation will be adapted to satisfy
    this protocol in a later step (A3.2+). Existing behavior must remain
    unchanged while we introduce this layer.
    """

    def load(self) -> MutableMapping[str, Any]:
        """
        Load the current registry state from the backing store.

        Implementations may choose their own internal schema so long as
        callers receive a mutable mapping that is compatible with the
        existing registry operations.
        """
        ...

    def save(self, data: MutableMapping[str, Any]) -> None:
        """
        Persist the given registry state into the backing store.

        Implementations must ensure that all existing registry operations
        see consistent data after this call completes.
        """
        ...
