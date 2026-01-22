#!/usr/bin/python3
"""
6-raise_exception_msg.py
Raises a NameError exception with a custom message.
"""


def raise_exception_msg(message=""):
    """
    Function that raises a NameError with a provided message.

    Args:
        message (str): The message to include in the exception
    """
    raise NameError(message)
