"""Kata: compress sentences.

Best practice by: worapolPan, DCoulter
def compress(sentence):
    ref = []
    for i in sentence.lower().split():
        if i not in ref:
            ref.append(i)
    return ''.join([str(ref.index(n)) for n in sentence.lower().split()])
"""


def compress(sentence):
    """Return possition of words."""
    words = sentence.lower().split()
    revised = []
    revised_again = []
    return_string = []
    for i in words:
        if i not in revised:
            revised.append(i)
    print (revised)
    for i in words:
        return_string.append(revised.index(i))
    for i in map(str, return_string):
        print(type(i))
        revised_again.append(i)
    return "".join(revised_again)
