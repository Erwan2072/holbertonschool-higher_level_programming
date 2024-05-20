#!/usr/bin/python3
"""
    Prints a square made of '#' characters.

    Parameters:
    size (int): The size of the square (both width and height).

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is less than 0.
"""

def print_square(size):
    """
    print a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
