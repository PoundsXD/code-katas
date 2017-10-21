"""Kata: love vs friendship.

Best practice by: acaccia, anter69, hwtdstrngls, kazk, rasmus_ri, ExhaleO2
def words_to_marks(s):
  return sum(ord(c)-96 for c in s)
"""


def words_to_marks(s):
    """Create score of word based on letters."""
    letter_vals = {}
    letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    letters = letters.split(' ')
    for i, x in enumerate(letters):
        letter_vals[x] = (i + 1)
    total = 0
    for i in s:
        total += letter_vals[i]
    return total
