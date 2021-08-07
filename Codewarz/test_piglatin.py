
from .piglatin import pig_latin

def test_map():
    assert pig_latin("map") == "apmay"


def test_egg():
    assert pig_latin("egg") == "eggway"


def test_spaghetti():
    assert pig_latin("Spaghetti") == "aghettispay"


def test_no_vowels():
    assert pig_latin("Yrtz") == "yrtzay"


def test_numbers_equal_none():
    assert pig_latin("123ay") is None


def test_ay_should_equal_ayway():
    assert pig_latin("ay") == "ayway"

def test_blank_equal_none():
    assert pig_latin("") is None

