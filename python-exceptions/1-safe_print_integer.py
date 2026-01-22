#!/usr/bin/python3
"""
1-safe_print_integer.py
Prints x integers of a list safely using try/except and only prints integers.
"""


def safe_print_integer(my_list=[], x=0):
    """
    Prints up to x integers of my_list on the same line.

    Args:
        my_list (list): List of elements (any type)
        x (int): Number of elements to try to print

    Returns:
        int: The number of integers actually printed
    """
    count = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            break
        except ValueError:
            continue
    print()
    return count
