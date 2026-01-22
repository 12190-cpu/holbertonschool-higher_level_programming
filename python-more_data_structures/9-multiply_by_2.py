#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 9-multiply_by_2
This module defines a function that returns a new dictionary
with all values multiplied by 2.
"""


def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values of the input dictionary
    multiplied by 2.

    Args:
        a_dictionary (dict): Dictionary with integer values.

    Returns:
        dict: New dictionary with values multiplied by 2.
    """
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict
