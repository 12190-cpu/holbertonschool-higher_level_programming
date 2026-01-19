#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 1-element_at
This module defines a function that retrieves an element from a list safely.
"""


def element_at(my_list, idx):
    """
    Retrieves an element from a list at a given index.

    Args:
        my_list (list): The list to retrieve the element from.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at index `idx` if it exists, otherwise None.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
