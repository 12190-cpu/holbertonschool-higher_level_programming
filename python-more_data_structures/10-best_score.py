#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 10-best_score
This module defines a function that returns the key with
the biggest integer value in a dictionary.
"""


def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value.

    Args:
        a_dictionary (dict): Dictionary with integer values.

    Returns:
        key: The key with the highest value, or None if dictionary is empty or None.
    """
    if not a_dictionary:
        return None

    best_key = None
    best_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return best_key
