"""Test the kata sum of nth terms."""

from nose.tools import assert_equals


def test_sum_of_nth():
    """Run code wars tests."""
    from sum_of_nth_terms import series_sum
    assert_equals(series_sum(1), "1.00")
    assert_equals(series_sum(2), "1.25")
    assert_equals(series_sum(3), "1.39")
