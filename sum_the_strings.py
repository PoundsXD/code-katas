"""Kata: sum the strings.

Best Practice By: Unnamed, tmxyz, azvm, mentalplex
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))
"""


def sum_str(a, b):
    """Sum strings a and b."""
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    return str(int(a) + int(b))
