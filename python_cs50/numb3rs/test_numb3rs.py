import pytest
from numb3rs import validate

def test_single_validate():
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True

def test_double_validate():
    assert validate("12.34.56.78") == True

def test_100_validate():
    assert validate("123.456.789.101") == False

def test_200_validate():
    assert validate("223.44.99.77") == True
    assert validate("275.777.254.256") == False

def test_string_validate():
    assert validate("cat") == False

