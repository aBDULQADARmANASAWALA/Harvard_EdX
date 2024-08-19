import pytest
from um import count

def test_1_count():
    assert count("um") == 1

def test_2_count():
    assert count("um?") == 1

def test_3_count():
    assert count("Um, thanks for the album.,") == 1

def test_4_count():
    assert count("Um, thanks, um...") == 2

def test_5_count():
    assert count("Wow, this is so yummy") == 0
