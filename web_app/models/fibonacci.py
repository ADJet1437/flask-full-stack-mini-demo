"""
This module implements general formula of Fibonacci sequence
"""
import math


def general_formula(n):
    """Apply the general formula of fibonacci sequence to calculate
    the value by given a integer n

    :param n: int, n >= 1
    :return: int
    """
    return 1/math.sqrt(5)*(((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n)

