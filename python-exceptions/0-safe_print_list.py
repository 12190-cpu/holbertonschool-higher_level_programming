#!/usr/bin/python3
"""
0-safe_print_list.py
Prints x elements of a list safely using try/except.
"""


def safe_print_list(my_list=[], x=0):
    """
    Prints up to x elements of my_list on the same line.

    Args:
        my_list (list): List of elements (any type)
        x (int): Number of elements to print

    Returns:
        int: The number of elements actually printed
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
