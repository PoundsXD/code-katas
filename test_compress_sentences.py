"""Test compress sentences kata."""

from nose.tools import assert_equals


def test_compression():
    """Test index words."""
    from compress_sentences import compress
    assert_equals(compress("The bumble bee"), "012")
    assert_equals(compress("the one bumble bee one bumble the bee"), "01231203")
    assert_equals(compress("WHY IS THERE BACON IN THE SOAP"), "0123456")
    assert_equals(compress("I need tacos otherwise I expload that haapens to me sometimes"), "01230456789")
    assert_equals(compress("I see said the blind man as he picked up his hammer and saw"), "012345678910111213")
    assert_equals(compress("Redundancy Redundancy more more I I"), "001122")
