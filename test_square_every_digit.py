"""Test square every digit kata."""

from nose.tools import assert_equals


def test_squares():
    """Test squares."""
    from square_every_digit import square_digits
    assert_equals(square_digits(9119), 811181)
    assert_equals(square_digits(9838), 8164964)
    assert_equals(square_digits(1876), 1644936)
    assert_equals(square_digits(119899), 1181648181)
    assert_equals(square_digits(287468), 46449163664)
