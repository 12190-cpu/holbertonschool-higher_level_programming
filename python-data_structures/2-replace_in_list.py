#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 2-replace_in_list
This module defines a function that replaces an element of a list at a specific position.
"""


def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific index.

    Args:
        my_list (list): The list to modify.
        idx (int): The index at which to replace an element.
        element: The new value to insert.

    Returns:
        list: The modified list, or the original list if idx is invalid.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
