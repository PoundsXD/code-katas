"""Test get the middle kata."""

from nose.tools import assert_equals


def test_get_middle():
    """Test slice middle."""
    from get_the_middle_character import get_middle
    assert_equals(get_middle("test"), "es")
    assert_equals(get_middle("testing"), "t")
    assert_equals(get_middle("middle"), "dd")
    assert_equals(get_middle("A"), "A")
    assert_equals(get_middle("of"), "of")
