#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 0-print_list_integer
This module defines a function that prints all integers of a list.
"""


def print_list_integer(my_list=[]):
    """
    Prints all integers of a list, one per line.

    Args:
        my_list (list): A list of integers.
    """
    for i in my_list:
        print("{:d}".format(i))
