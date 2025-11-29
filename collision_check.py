# collision_check.py

from date_utils import icu_date
from db_queries import find_persona_by_date
from open_link import open_link

COLLISION_URL = "https://example.com/persona-collision"

def check_same_day_persona(persona: str):
    """
    After registering a persona, check whether this persona
    has multiple entries on the same icu_date().
    """
    stamp = icu_date()
    matches = find_persona_by_date(persona, stamp)

    if len(matches) > 1:
        open_link(COLLISION_URL)
        return True

    return False
