#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 4-only_diff_elements
This module defines a function that returns a set of all elements
present in only one of two sets.
"""


def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A new set containing elements unique to each input set.
    """
    return set_1 ^ set_2
