# daydir/DayDir.py

from pathlib import Path
from logger import info, fail
from .DayDirSettings import DayDirSettings, DayDirSettingsException


class DayDirError(Exception):
    """Raised when DayDir cannot be constructed."""
    pass


class DayDir:
    def __init__(self, settings_file):
        try:
            self.settings = DayDirSettings(settings_file)
        except DayDirSettingsException as e:
            fail(f"DayDir: settings invalid → {e}")
            raise DayDirError(f"Invalid settings: {e}")

        self.root = Path(self.settings.get_daydir_root())
        info(f"DayDir: settings loaded from {settings_file}")
        info(f"DayDir: resolved root = {self.root}")

        self._sanity_check_root()

    def _sanity_check_root(self):
        if not self.root.exists():
            fail(f"DayDir: root does not exist → {self.root}")
            raise DayDirError(f"Root does not exist: {self.root}")

        if not self.root.is_dir():
            fail(f"DayDir: root is not a directory → {self.root}")
            raise DayDirError(f"Root is not a directory: {self.root}")

        info(f"DayDir: root validated OK → {self.root}")

    def __repr__(self):
        return f"<DayDir root={self.root}>"
