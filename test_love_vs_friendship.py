"""Test love vs friendship kata."""


from nose.tools import assert_equals


def test_score_word():
    """Test word scores."""
    from love_vs_friendship import words_to_marks
    assert_equals(words_to_marks('attitude'), 100)
    assert_equals(words_to_marks('friends'), 75)
    assert_equals(words_to_marks('family'), 66)
    assert_equals(words_to_marks('selfness'), 99)
    assert_equals(words_to_marks('knowledge'), 96)
    assert_equals(words_to_marks('anihilation'), 112)
    assert_equals(words_to_marks('domination'), 114)
    assert_equals(words_to_marks('sublime'), 81)
    assert_equals(words_to_marks('python'), 98)
