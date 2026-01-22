#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 1-search_replace
This module defines a function that replaces all occurrences of an element
by another in a new list.
"""


def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of 'search' by 'replace' in a new list.

    Args:
        my_list (list): The initial list.
        search: The element to replace.
        replace: The new element to insert.

    Returns:
        list: A new list with the replacements applied.
    """
    return [replace if x == search else x for x in my_list]
