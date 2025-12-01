import json
import os

class DayDirSettingsException(Exception):
    pass

class DayDirSettings:
    def __init__(self, settings_file):
        self._settings_file = settings_file
        self._data = None
        self.read_settings()

    def read_settings(self):
        if not os.path.exists(self._settings_file):
            raise DayDirSettingsException(f"Settings file not found: {self._settings_file}")

        raw = open(self._settings_file, "r").read()
        if not raw.strip():
            raise DayDirSettingsException("Settings file is empty")

        try:
            self._data = json.loads(raw)
        except json.JSONDecodeError as e:
            raise DayDirSettingsException(f"Invalid JSON: {e}")

        self._sanity_check()

    def _sanity_check(self):
        root = self._data.get("dayDirRoot", None)

        if root is None:
            print("warn: Missing 'dayDirRoot' in settings.")
            return

        if root == "":
            print("warn: 'dayDirRoot' is empty.")
            return

        if not os.path.exists(root):
            print(f"warn: dayDirRoot path does not exist: {root}")
            return

        if not os.path.isdir(root):
            print(f"warn: dayDirRoot exists but is not a directory: {root}")
            return

