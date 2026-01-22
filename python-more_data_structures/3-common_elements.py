#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 3-common_elements
This module defines a function that returns a set of common elements in two sets.
"""


def common_elements(set_1, set_2):
    """
    Returns a set of common elements between two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A new set containing elements found in both sets.
    """
    return set_1 & set_2
