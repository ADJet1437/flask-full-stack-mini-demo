"""
This module implements factorial function by definition
"""


def factorial(n):
    """Provided a number n, calculate it's factorial.
    E.x. if n > 2, n! = n*(n-1)*(n-2)...2

    :param n: int
    :return:
    """
    if n== 0 or n== 1:
        return 1
    else:
        return n * factorial(n - 1)