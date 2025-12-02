# daydir/DayDir.py

from pathlib import Path
from datetime import datetime
from logger import info, fail
from .DayDirSettings import DayDirSettings, DayDirSettingsException

DAYDIR_TIME_FORMAT = "%Y-%m-%d-%a"


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
        self.day_directories = []

    def _sanity_check_root(self):
        if not self.root.exists():
            fail(f"DayDir: root does not exist → {self.root}")
            raise DayDirError(f"Root does not exist: {self.root}")

        if not self.root.is_dir():
            fail(f"DayDir: root is not a directory → {self.root}")
            raise DayDirError(f"Root is not a directory: {self.root}")

        info(f"DayDir: root validated OK → {self.root}")

    def init(self):
        """
        Discover existing day directories under the configured root.
        """
        self.day_directories = self._find_day_directories()
        if not self.day_directories:
            info(f"DayDir: no day directories found under {self.root}")
        else:
            info(f"DayDir: found {len(self.day_directories)} day directories under {self.root}")
            for d in self.day_directories:
                info(f"DayDir: day directory → {d}")
        return self.day_directories

    def _find_day_directories(self):
        matches = []
        for entry in self.root.iterdir():
            if not entry.is_dir():
                continue
            try:
                datetime.strptime(entry.name, DAYDIR_TIME_FORMAT)
                matches.append(entry)
            except ValueError:
                continue
        return sorted(matches)

    def createNewDay(self):
        """
        Create a new day directory using the current date and DAYDIR_TIME_FORMAT.
        """
        dirname = datetime.now().strftime(DAYDIR_TIME_FORMAT)
        target = self.root / dirname

        if target.exists():
            if not target.is_dir():
                fail(f"DayDir: cannot create day directory, file exists → {target}")
                raise DayDirError(f"Cannot create day directory; file exists at {target}")
            info(f"DayDir: day directory already exists → {target}")
        else:
            try:
                target.mkdir(parents=False, exist_ok=False)
                info(f"DayDir: created day directory → {target}")
            except Exception as e:
                fail(f"DayDir: failed to create day directory → {e}")
                raise DayDirError(f"Failed to create day directory: {e}")

        # Keep internal list in sync
        if target not in self.day_directories:
            self.day_directories.append(target)
            self.day_directories = sorted(self.day_directories)

        return target

    def createNewDayEntry(self):
        """
        Create a new JSON entry inside today's day directory.

        The entry file is named with the same DAYDIR_TIME_FORMAT, plus .json.
        If the file exists, it is left untouched and returned.
        """
        day_dir = self.createNewDay()
        filename = f"{day_dir.name}.json"
        json_path = day_dir / filename

        if json_path.exists():
            if json_path.is_file():
                info(f"DayDir: day entry already exists → {json_path}")
                return json_path
            fail(f"DayDir: cannot create day entry, path is not a file → {json_path}")
            raise DayDirError(f"Cannot create day entry; path is not a file: {json_path}")

        try:
            json_path.write_text("{}", encoding="utf-8")
            info(f"DayDir: created day entry → {json_path}")
        except Exception as e:
            fail(f"DayDir: failed to create day entry → {e}")
            raise DayDirError(f"Failed to create day entry: {e}")

        return json_path

    def __repr__(self):
        return f"<DayDir root={self.root}>"
