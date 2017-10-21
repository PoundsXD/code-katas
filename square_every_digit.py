"""Kata: square every digit.

Best practice by: djm4686, Reserved_name, 2-up, DmitriyVakarin
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
"""


def square_digits(num):
    """Square digits."""
    num = str(num)
    final_num = ""
    for i in num:
        final_num = final_num + str((int(i) ** 2))
    return int(final_num)
