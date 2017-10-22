"""Kata: how sexy is your name.

Best practice by: zebulan
def sexy_name(name):
    name_score = sum(SCORES.get(a, 0) for a in name.upper())
    if name_score >= 600:
        return 'THE ULTIMATE SEXIEST'
    elif name_score >= 301:
        return 'VERY SEXY'
    elif name_score >= 61:
        return 'PRETTY SEXY'
    return 'NOT TOO SEXY'
"""

SCORES = {'A': 100, 'B': 14, 'C': 9, 'D': 28, 'E': 145, 'F': 12, 'G': 3,
          'H': 10, 'I': 200, 'J': 100, 'K': 114, 'L': 100, 'M': 25,
          'N': 450, 'O': 80, 'P': 2, 'Q': 12, 'R': 400, 'S': 113, 'T': 405,
          'U': 11, 'V': 10, 'W': 10, 'X': 3, 'Y': 210, 'Z': 23}


def sexy_name(name):
    """Score name for sexyness."""
    sexy_score = 0
    name = name.replace(" ", "").upper()
    if name == '' or name == ' ':
        return 'NOT TOO SEXY'
    for i in name:
        sexy_score = SCORES[i] + sexy_score
    if(sexy_score >= 600):
        return 'THE ULTIMATE SEXIEST'
    elif(301 <= sexy_score <= 599):
        return 'VERY SEXY'
    elif(61 <= sexy_score <= 300):
        return 'PRETTY SEXY'
    elif(sexy_score <= 60):
        return 'NOT TOO SEXY'
