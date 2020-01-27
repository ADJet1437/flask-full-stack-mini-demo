"""
This module implements ackermann function by definition
"""


def ackermann(m, n):
    """Accept integer m and n, and calculate ackermann
    result A(m, n)

    :param m: int
    :param n: int
    :return:
    """
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1, ackermann(m,n-1))