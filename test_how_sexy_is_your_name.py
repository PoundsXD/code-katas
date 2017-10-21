"""Test sexy name kata."""

from nose.tools import assert_equals


def test_sexyness():
    """Calculate sexyness."""
    from how_sexy_is_your_name import sexy_name
    assert_equals(sexy_name('GUV'), 'NOT TOO SEXY')
    assert_equals(sexy_name('PHUG'), "NOT TOO SEXY")
    assert_equals(sexy_name('FFFFF'), 'NOT TOO SEXY')
    assert_equals(sexy_name(''), "NOT TOO SEXY")
    assert_equals(sexy_name('PHUG'), "NOT TOO SEXY")
    assert_equals(sexy_name('BOB'), "PRETTY SEXY")
    assert_equals(sexy_name('JLJ'), 'PRETTY SEXY')
    assert_equals(sexy_name('HHHHHU'), 'PRETTY SEXY')
    assert_equals(sexy_name('BOB'), "PRETTY SEXY")
    assert_equals(sexy_name('WWWWWU'), "PRETTY SEXY")
    assert_equals(sexy_name('YOU'), 'VERY SEXY')
    assert_equals(sexy_name('FABIO'), "VERY SEXY")
    assert_equals(sexy_name('ARUUUUUUUUU'), 'VERY SEXY')
    assert_equals(sexy_name('ROBBY'), 'THE ULTIMATE SEXIEST')
    assert_equals(sexy_name('SAMANTHA'), 'THE ULTIMATE SEXIEST')
    assert_equals(sexy_name('DONALD TRUMP'), "THE ULTIMATE SEXIEST")
    assert_equals(sexy_name('BILL GATES'), "THE ULTIMATE SEXIEST")
    assert_equals(sexy_name('SCARLETT JOHANSSON'), "THE ULTIMATE SEXIEST")
    assert_equals(sexy_name('CODEWARS'), "THE ULTIMATE SEXIEST")
    assert_equals(sexy_name('PAMELA ANDERSON'), "THE ULTIMATE SEXIEST")
    assert_equals(sexy_name('you'), 'VERY SEXY')
    assert_equals(sexy_name('Codewars'), "THE ULTIMATE SEXIEST")
    assert_equals(sexy_name('Carmellina'), "THE ULTIMATE SEXIEST")
    assert_equals(sexy_name('Eamon'), "THE ULTIMATE SEXIEST")
    assert_equals(sexy_name('Kellianna'), "THE ULTIMATE SEXIEST")
    assert_equals(sexy_name('PoundsXD'), "THE ULTIMATE SEXIEST")
