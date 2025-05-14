from __future__ import annotations

from enum import Enum, auto
import re

_US_TO_FR_RE = re.compile(r"([0-9]+)-([0-9]+)-([0-9]+)")

def us_to_fr(text: str) -> str:
    result = ""
    last_pos = 0
    for date_match in _US_TO_FR_RE.finditer(text):
        # copy since the last position unchanged
        result += text[last_pos:date_match.start(0)]
        # insert the new formatted date
        month, day, year = date_match.groups()
        result += f"{day}/{month}/{year}"
        # update last_pos to be at the *end* of the match
        last_pos = date_match.end(0)

    # copy since the last match until the end of the text
    result += text[last_pos:]

    return result

class Format(Enum):
    FR = auto()
    EN = auto()
    HU = auto()

def format_date(format: Format, year: str, month: str, day: str) -> str:
    match format:
        case Format.FR: return f"{day}/{month}/{year}"
        case Format.EN: return f"{month}-{day}-{year}"
        case Format.HU: return f"{year}-{month}-{day}"

_ANY_DATE_RE = re.compile(
    r"([0-9]{1,2})/([0-9]{1,2})/([0-9]{1,4})|" + # FR
    r"([0-9]{1,2})-([0-9]{1,2})-([0-9]{1,4})|" + # EN
    r"([0-9]{1,4})-([0-9]{1,2})-([0-9]{1,2})" # HU
)

def translate_all(text: str, target_format: Format) -> str:
    result = ""
    last_pos = 0

    for date_match in _ANY_DATE_RE.finditer(text):
        # copy since the last position unchanged
        result += text[last_pos:date_match.start(0)]
        # extract the parts, depending on which groups matched
        match date_match.groups():
            case (day, month, year, None, None, None, None, None, None): pass
            case (None, None, None, month, day, year, None, None, None): pass
            case (None, None, None, None, None, None, year, month, day): pass
            case groups:
                assert False, f"did not expect groups: {repr(groups)}"
        # insert the new formatted date
        result += format_date(target_format, year, month, day)
        # update last_pos to be at the *end* of the match
        last_pos = date_match.end(0)

    # copy since the last match until the end of the text
    result += text[last_pos:]

    return result
