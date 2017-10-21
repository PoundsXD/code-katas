r"""Kata: nickname generator.

Best practice by: Blind4Basics
def nickname_generator(name):
    return "Error: Name too short" if len(name) < 4 else name[:3+(name[2]\
    in "aeiuo")]
"""


def nickname_generator(name):
    """Create a nickname."""
    print(name)
    import re
    regex = r'[a, e, i, o, u]'
    if(len(name) <= 3):
        return 'Error: Name too short'
    if(re.search(regex, name[2])):
        return name[:4]
    else:
        return name[:3]
