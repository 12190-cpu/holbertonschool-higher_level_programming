#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 5-no_c
This module defines a function that removes all characters 'c' and 'C' from a string.
"""


def no_c(my_string):
    """
    Removes all characters 'c' and 'C' from a string.

    Args:
        my_string (str): The original string.

    Returns:
        str: A new string without any 'c' or 'C'.
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
