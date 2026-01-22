#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 8-simple_delete
This module defines a function that deletes a key in a dictionary
if it exists.
"""


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary if it exists.

    Args:
        a_dictionary (dict): The dictionary to modify.
        key (str): The key to delete.

    Returns:
        dict: The updated dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
