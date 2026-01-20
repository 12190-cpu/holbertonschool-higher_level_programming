#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 9-max_integer
This module defines a function that finds the biggest integer in a list.
"""


def max_integer(my_list=[]):
    """
    Finds and returns the biggest integer in a list.

    Args:
        my_list (list): A list of integers.

    Returns:
        int: The biggest integer in the list, or None if the list is empty.
    """
    if len(my_list) == 0:
        return None

    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
