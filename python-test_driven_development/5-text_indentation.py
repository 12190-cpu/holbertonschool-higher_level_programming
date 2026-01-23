#!/usr/bin/python3
"""
This module defines a function that prints a text with
two new lines after each '.', '?' and ':' character.

The function removes unnecessary spaces at the beginning
and end of each printed line.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':' characters.

    Args:
        text (str): The input text to format.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    result = ""
    start = 0

    for c in text:
        result += c
        if c in chars:
            result = result.strip()
            print(result)
            print()
            result = ""
    if result.strip() != "":
        print(result.strip(), end="")
