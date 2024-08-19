import pytest

from fuel import convert, gauge

def test_str_convert():
    with pytest.raises(ValueError):
        assert convert("dog")

def test_fraction_convert():
    with pytest.raises(ValueError):
        assert convert("12")

def test_improper_fraction_convert():
    with pytest.raises(ValueError):
        assert convert("2/1")

def test_zero_division_convert():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")

def test_valid_convert():
    assert convert("1/2") == 50
    assert convert("2/3") == 67

def test_E_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_F_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_valid_gauge():
    assert gauge(50) == "50%"
    assert gauge(20) == "20%"
