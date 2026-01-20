#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 10-divisible_by_2
This module defines a function that finds all multiples of 2 in a list.
"""


def divisible_by_2(my_list=[]):
    """
    Returns a new list with True or False depending on whether
    each integer in the original list is a multiple of 2.

    Args:
        my_list (list): A list of integers.

    Returns:
        list: A list of booleans where True means divisible by 2.
    """
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
