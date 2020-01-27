"""
This test module is to test all the functions / algorithms which have been
implemented in models
"""

import random

import pytest
from sympy import *

from web_app.models.ackermann import ackermann
from web_app.models.factorial import factorial as fac
from web_app.models.fibonacci import general_formula


MIN = 1
MAX = 50


@pytest.mark.function
def test_ackermann_function():
    """

    :return:
    """
    assert ackermann(3, 4) == 125


@pytest.mark.function
def test_fibonacci_general_formula():
    """Compare values between general formula and standard fibonacci
    function of sympy. Due to different algorithm implementation, when
    n gets larger, the value difference will become bigger

    :return:
    """
    n = random.randint(MIN, MAX)
    assert int(fibonacci(n)) == int(general_formula(n))


@pytest.mark.function
def test_factorial_function():
    """Our internal factorial function is implemented by definition,
    for safe, we can compare it to sympy standard factorial

    :return:
    """
    n = random.randint(MIN, MAX)
    assert fac(n) == factorial(n)
