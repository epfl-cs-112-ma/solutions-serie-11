from __future__ import annotations

from datetranslator import *

def test_us_to_fr() -> None:
    assert us_to_fr("4-5-2010") == "5/4/2010"
    assert us_to_fr("nothing") == "nothing"
    assert us_to_fr("abc 4-5-2010 def 12-20-2025 ghi") == "abc 5/4/2010 def 20/12/2025 ghi"

def test_translate_all() -> None:
    assert translate_all("abc 4-5-2010 def 20/12/2025 ghi 2020-2-8", Format.FR) == "abc 5/4/2010 def 20/12/2025 ghi 8/2/2020"
    assert translate_all("abc 4-5-2010 def 20/12/2025 ghi 2020-2-8", Format.EN) == "abc 4-5-2010 def 12-20-2025 ghi 2-8-2020"
    assert translate_all("abc 4-5-2010 def 20/12/2025 ghi 2020-2-8", Format.HU) == "abc 2010-4-5 def 2025-12-20 ghi 2020-2-8"
