r"""Kata: grouped by commas.

Best practice by: mbaxa, SwingKing, HEXecutive, ChristianECooper, gvbgduh,\
EastAustinian (plus 145 more warriors)
def group_by_commas(n):
    return '{:,}'.format(n)
"""


def group_by_commas(n):
    """Add commas in thousandth places."""
    n = format(n, ',d')
    return n
