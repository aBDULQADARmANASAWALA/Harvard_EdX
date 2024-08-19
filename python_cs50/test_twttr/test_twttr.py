import pytest

from twttr import shorten

def test_uppercase_shorten():
    assert shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"

def test_lowercase_shorten():
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_punct_shorten():
    assert shorten("a,e.i/o'u") == ",./'"

def test_num_shorten():
    assert shorten("a1e2i3o4u5") == "12345"

