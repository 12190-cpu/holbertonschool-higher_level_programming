#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 6-print_sorted_dictionary
This module defines a function that prints a dictionary sorted by keys.
"""


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
        a_dictionary (dict): The dictionary to print.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
