# collision_check.py

from date_utils import icu_date
from db_queries import find_persona_by_date
from open_link import open_link

def check_same_day_persona(persona: str, url: str):
    stamp = icu_date()
    matches = find_persona_by_date(persona, stamp)

    if len(matches) > 1:
        open_link(url)   # open the actual registered URL
        return True

    return False
