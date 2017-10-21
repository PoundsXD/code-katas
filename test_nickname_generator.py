"""Test nickname generator from codewars."""

from nose.tools import assert_equals


def test_nickname():
    """Test nick names."""
    from nickname_generator import nickname_generator
    assert_equals(nickname_generator("Jimmy"), "Jim")
    assert_equals(nickname_generator("Samantha"), "Sam")
    assert_equals(nickname_generator("Sam"), "Error: Name too short")
    assert_equals(nickname_generator("Kayne"), "Kay", "'y' is not a vowel")
    assert_equals(nickname_generator("Melissa"), "Mel")
    assert_equals(nickname_generator("James"), "Jam")
    assert_equals(nickname_generator("Carmellina"), "Car")
    assert_equals(nickname_generator("Eamon"), "Eam")
    assert_equals(nickname_generator("Kellianna"), "Kel")
    assert_equals(nickname_generator("Jerry"), "Jer")
