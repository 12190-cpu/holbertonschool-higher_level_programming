#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 11-delete_at
This module defines a function that deletes an item at a specific position in a list.
"""


def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Args:
        my_list (list): The list from which to delete the element.
        idx (int): The index of the element to delete.

    Returns:
        list: The same list after deletion, or the original list
              if the index is invalid.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list
