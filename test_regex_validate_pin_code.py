"""."""


from nose.tools import assert_equals


def test_pin_number():
    """."""
    from regex_validate_pin_code import validate_pin
    assert_equals(validate_pin("1"), False, "Wrong output for '1'")
    assert_equals(validate_pin("12"), False, "Wrong output for '12'")
    assert_equals(validate_pin("123"), False, "Wrong output for '123'")
    assert_equals(validate_pin("12345"), False, "Wrong output for '12345'")
    assert_equals(validate_pin("1234567"), False, "Wrong output for '1234567'")
    assert_equals(validate_pin("-1234"), False, "Wrong output for '-1234'")
    assert_equals(validate_pin("1.234"), False, "Wrong output for '1.234'")
    assert_equals(validate_pin("a234"), False, "Wrong output for 'a234'")
    assert_equals(validate_pin(".234"), False, "Wrong output for '.234'")
    assert_equals(validate_pin("1234"), True, "Wrong output for '1234'")
    assert_equals(validate_pin("0000"), True, "Wrong output for '0000'")
    assert_equals(validate_pin("1111"), True, "Wrong output for '1111'")
    assert_equals(validate_pin("123456"), True, "Wrong output for '123456'")
    assert_equals(validate_pin("098765"), True, "Wrong output for '098765'")
    assert_equals(validate_pin("000000"), True, "Wrong output for '000000'")
    assert_equals(validate_pin("123456"), True, "Wrong output for '123456'")
    assert_equals(validate_pin("090909"), True, "Wrong output for '090909'")

    assert_equals(validate_pin("998936"), True, "Wrong output for '998936'")
    assert_equals(validate_pin("43689"), False, "Wrong output for '43689'")
    assert_equals(validate_pin("2030"), True, "Wrong output for '2030'")
    assert_equals(validate_pin("..9080"), False, "Wrong output for '..9080'")
