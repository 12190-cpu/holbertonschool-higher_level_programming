#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module 8-multiple_returns
This module defines a function that returns a tuple with the length
of a string and its first character.
"""


def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: (length of string, first character or None if empty)
    """
    length = len(sentence)
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return (length, first_char)
