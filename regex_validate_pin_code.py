r"""Kata: regex validate pin code.

Best practice by: CrazyMerlyn, pivek303, lechevalier, aytrack, bugaevc,\
andriis(plus 60 more warriors)
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
"""


def validate_pin(pin):
    """Validate pin number for length and numeric values."""
    print(pin)
    import re
    regex = r"\D"
    if(len(pin) == 4 or len(pin) == 6):
        if re.search(regex, pin):
            return False
        else:
            return True
    elif(len(pin) != 4 or len(pin) != 6):
        return False
