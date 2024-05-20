#!/usr/bin/python3
""" Return the addition of two integer"""

def add_integer(a, b=98):
    """Computes the sum of two integers
        return error if a or b is not integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError ("a must or b is not integer")
    if not isinstance(b, (int, float)):
        raise TypeError ("b must or b is not integer")

    return int(a) + int(b)
