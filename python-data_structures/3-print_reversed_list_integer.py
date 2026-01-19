#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 3-print_reversed_list_integer
This module defines a function that prints all integers of a list in reverse order.
"""


def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list in reverse order, one per line.

    Args:
        my_list (list): A list of integers.
    """
    if my_list is not None:
        for i in reversed(my_list):
            print("{:d}".format(i))
