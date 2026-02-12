#!/usr/bin/python3
"""Module that defines a function to append text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF-8 text file and return number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append at the end of the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
