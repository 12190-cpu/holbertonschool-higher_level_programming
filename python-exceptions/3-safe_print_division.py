#!/usr/bin/python3
"""
3-safe_print_division.py
Divides two integers safely and prints the result.
"""


def safe_print_division(a, b):
    """
    Divides a by b, prints the result, and returns it.

    Args:
        a (int): Dividend
        b (int): Divisor

    Returns:
        float: Result of the division, or None if division fails
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
