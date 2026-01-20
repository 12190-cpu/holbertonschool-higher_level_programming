#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 7-add_tuple
This module defines a function that adds two tuples.
"""


def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples.

    Each tuple must contain integers, but may have less or more than 2 elements.
    Missing values are replaced by 0, and only the first two elements are used.

    Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.

    Returns:
        tuple: A tuple with 2 integers, representing the element-wise sum.
    """
    # Ensure both tuples have at least 2 elements by padding with zeros
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Take only the first two elements and add them
    sum_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum_tuple
