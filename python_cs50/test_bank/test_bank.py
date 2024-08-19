import pytest
from bank import value


def test_hello_value():
    assert value("Hello, greetings") == 0
    assert value("hello, greetings") == 0
    assert value("HELLO, GREETINGS") == 0

def test_h_value1():
    assert value("Hey, nice toh meet you") == 20
    assert value("hey, nice toh meet you") == 20
    assert value("HEY, NICE TO MEET YOU") == 20

def test_h_value2():
    assert value("How's everything") == 20
    assert value("how's everything") == 20
    assert value("HOW'S EVERYTHING") == 20

def test_any_value():
    assert value("Nice to meet you") == 100
    assert value("nice to meet you") == 100
    assert value("NICE TO MEET YOU") == 100
