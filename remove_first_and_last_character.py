"""Kata: remove first and last character.

Best practice by: zebulan, Unnamed, jake9066, NaMe613, chessmonger2112, arainho (plus 1065 more warriors)
def remove_char(s):
    return s[1 : -1]
"""


def remove_char(s):
    """Slice first and last character off string."""
    v = s[1:(len(s) - 1)]
    return v
