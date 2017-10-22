"""Test kata grouped by commas."""


from nose.tools import assert_equals


def test_add_commas():
    """Test grouped function."""
    from grouped_by_commas import group_by_commas
    assert_equals(group_by_commas(1), '1')
    assert_equals(group_by_commas(10), '10')
    assert_equals(group_by_commas(100), '100')
    assert_equals(group_by_commas(1000), '1,000')
    assert_equals(group_by_commas(10000), '10,000')
    assert_equals(group_by_commas(100000), '100,000')
    assert_equals(group_by_commas(1000000), '1,000,000')
    assert_equals(group_by_commas(35235235), '35,235,235')
    assert_equals(group_by_commas(490), '490')
    assert_equals(group_by_commas(58900), '58,900')
    assert_equals(group_by_commas(12345), '12,345')
    assert_equals(group_by_commas(9800489), '9,800,489')
