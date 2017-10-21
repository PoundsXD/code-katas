"""Test remove first last kata."""

from nose.tools import assert_equals


def test_removal():
    """Test remove."""
    from remove_first_and_last_character import remove_char
    assert_equals(remove_char('eloquent'), 'loquen')
    assert_equals(remove_char('country'), 'ountr')
    assert_equals(remove_char('person'), 'erso')
    assert_equals(remove_char('place'), 'lac')
    assert_equals(remove_char('ok'), '')
    assert_equals(remove_char('googlespadoodle'), 'ooglespadoodl')
    assert_equals(remove_char('purplegoo'), 'urplego')
    assert_equals(remove_char('zim'), 'i')
    assert_equals(remove_char('gir'), 'i')
