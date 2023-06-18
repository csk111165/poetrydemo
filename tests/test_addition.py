"""
Test module for the addition
"""
from myproject.addition import add_numbers


def test_additoin():
    assert add_numbers(1, 2) == 30
