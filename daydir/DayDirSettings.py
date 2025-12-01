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

    def return_settings_as_json(self):
        return json.dumps(self._data, indent=2)

    def _sanity_check(self):
        root = self._data.get("dayDirRoot", None)

        if root is None:
            raise DayDirSettingsException(f"Invalid settings: Missing 'dayDirRoot' in settings.")

        if root == "":
            raise DayDirSettingsException(f"Invalid settings: 'dayDirRoot' is empty.")

        if not os.path.exists(root):
            raise DayDirSettingsException(f"Invalid settings: dayDirRoot path does not exist: {root}")

        if not os.path.isdir(root):
            raise DayDirSettingsException(f"Invalid settings: dayDirRoot exists but is not a directory: {root}")

