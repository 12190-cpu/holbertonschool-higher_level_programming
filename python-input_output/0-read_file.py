#!/usr/bin/python3
"""Module that defines a function to read a UTF-8 text file and print it to stdout."""

def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout.

    Args:
        filename (str): Path to the UTF-8 encoded text file. Default is an empty string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
