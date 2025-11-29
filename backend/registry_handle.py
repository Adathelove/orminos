class RegistryHandle:
    """
    Minimal façade for the in-memory registry map.
    Does not alter semantics; simply provides a stable surface
    for future day-directory logic.
    """
    def __init__(self, data: dict):
        self.data = data

    def unwrap(self) -> dict:
        return self.data
