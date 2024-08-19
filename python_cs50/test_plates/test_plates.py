import pytest
from plates import is_valid

def test_first2letters_valid():
    assert is_valid("123456") == False
    assert is_valid("A12345") == False
    assert is_valid("AB2134") == True

def test_len_valid():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABCDEFGH") == False

def test_num_valid():
    assert is_valid("ABCDEF") == True
    assert is_valid("ABC321") == True
    assert is_valid("ABC32A") == False
    assert is_valid("ABC000") == False
    assert is_valid("AB0321") == False
    assert is_valid("AB032A") == False

def test_punct_valid():
    assert is_valid("AB12.,") == False
    assert is_valid("AB12/'") == False

