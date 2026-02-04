#!/usr/bin/python3
"""
Module that defines a function to check if an object
is an instance of a class or inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if it is an instance
    of a class that inherited from, the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
