import pytest

from src.sonar_poc.some_code import do_something, do_another


def test_do_something():
    assert do_something(1, 2) is False


def test_do_another():
    assert do_another(1, 2) is False


def test_do_anotherr():
    assert do_another(2, 2) is True
