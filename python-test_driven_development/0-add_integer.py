#!/usr/bin/python3
"""
This module provides a function that adds two integers.

The function ensures the inputs are integers or floats,
casts floats to integers, and raises errors for invalid inputs.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum as an integer.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or a float.

    Returns:
        int: The integer sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
