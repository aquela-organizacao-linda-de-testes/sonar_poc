import pytest

from src.sonar_poc.some_code import do_something


def test_do_something():
    assert do_something(1, 2) is False
