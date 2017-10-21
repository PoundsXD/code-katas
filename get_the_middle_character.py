r"""Kata: get the middle character.

Best practice by: hiasen, kit9ra, GNX, niedyszyn, RandomJack, pstryq (plus 40\
more warriors)
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
"""


def get_middle(s):
    """Slice the middle character(s) out."""
    if(len(s) == 1 or len(s) == 2):
        return s
    elif((len(s) % 2) == 0):
        return s[((len(s) / 2) - 1):((len(s) / 2) + 1)]
    elif((len(s) % 2) == 1):
        return s[(len(s) / 2):((len(s) / 2) + 1)]
