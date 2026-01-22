#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 2-uniq_add
This module defines a function that adds all unique integers in a list.
"""


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once per integer).

    Args:
        my_list (list): A list of integers.

    Returns:
        int: The sum of all unique integers in the list.
    """
    unique_integers = set(my_list)
    return sum(unique_integers)
