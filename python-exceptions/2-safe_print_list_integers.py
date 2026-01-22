#!/usr/bin/python3
"""
2-safe_print_list_integers.py
Prints x integers of a list safely using try/except and casts when possible.
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints up to x integers of my_list on the same line.
    Casts elements to int if possible.

    Args:
        my_list (list): List of elements (any type)
        x (int): Number of elements to try to print

    Returns:
        int: The number of integers actually printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(int(my_list[i])), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return count
