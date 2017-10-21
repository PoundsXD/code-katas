"""Test sum the string codewars."""

from nose.tools import assert_equals


def test_sum_str():
    """Test sum_str."""
    from sum_the_strings import sum_str
    assert_equals(sum_str("4", "5"), "9")
    assert_equals(sum_str("34", "5"), "39")
    assert_equals(sum_str("44", "20"), "64")
    assert_equals(sum_str("34", "20"), "54")
    assert_equals(sum_str("24", "20"), "44")
    assert_equals(sum_str("14", "20"), "34")
    assert_equals(sum_str("", "20"), "20")
