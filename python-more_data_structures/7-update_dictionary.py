#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 7-update_dictionary
This module defines a function that replaces or adds
a key/value pair in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value pair in a dictionary.

    Args:
        a_dictionary (dict): The dictionary to update.
        key (str): The key to replace or add.
        value: The value to associate with the key.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
