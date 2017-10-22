"""Kata: som of the nth terms.

Best practice by:MMMAAANNN, doctornick5, Slx64, ninja37, FablehavenGeek, nabrarpour4 (plus 18 more warriors)
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    """Sum 1 plus nth values."""
    total = 1
    div_vals = []
    if(n == 0):
        return "0.00"
    if(n == 1):
        return "1.00"
    for i in range(n - 1):
        div_vals.append(((i + 1) * 3) + 1)
        total += (1 / div_vals[i])
        print(total)
    return str(format(total, '.2f'))
