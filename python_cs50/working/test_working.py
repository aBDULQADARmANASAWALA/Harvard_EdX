import pytest
from working import convert

def test_long_convert():
    assert convert("9:42 AM to 5:00 PM") == "09:42 to 17:00"
    assert convert("9:00 PM to 5:08 AM") == "21:00 to 05:08"
    assert convert("9:00 AM to 5:00 AM") == "09:00 to 05:00"
    assert convert("5:00 PM to 9:00 PM") == "17:00 to 21:00"

def test_short_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"

def test_both_convert():
    assert convert("9 AM to 5:55 AM") == "09:00 to 05:55"
    assert convert("9:00 AM to 5 AM") == "09:00 to 05:00"

def test_invalid_convert():
    with pytest.raises(ValueError):
        assert convert("9 AM 5:79 AM")
    with pytest.raises(ValueError):
        assert convert("9:60 AM - 5:60 PM")
    with pytest.raises(ValueError):
        assert convert("9 AM to 5:79 AM")
    with pytest.raises(ValueError):
        assert convert("13 PM to 5 AM")
    with pytest.raises(ValueError):
        assert convert("cat")
