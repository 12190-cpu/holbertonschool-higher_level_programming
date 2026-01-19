#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 4-new_in_list
This module defines a function that replaces an element in a list
at a specific position without modifying the original list.
"""


def new_in_list(my_list, idx, element):
    """
    Returns a new list with an element replaced at a specific index.

    Args:
        my_list (list): The original list.
        idx (int): The index of the element to replace.
        element: The new value to insert.

    Returns:
        list: A new list with the modification, or a copy of the
              original list if the index is invalid.
    """
    if my_list is None:
        return None

    # Create a shallow copy of the original list
    new_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list[idx] = element
    return new_list
