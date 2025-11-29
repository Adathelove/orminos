from datetime import datetime

def day_directory_name(ts=None):
    """
    Return directory name in format:
        YYYY-MM-DD-EEE
    Using current date if ts is None.
    """
    if ts is None:
        ts = datetime.now()

    weekday = ts.strftime("%a")       # EEE
    return ts.strftime(f"%Y-%m-%d-{weekday}")

