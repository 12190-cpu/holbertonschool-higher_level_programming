#!/usr/bin/python3
"""Function that returns the dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """
    Returns a dictionary containing all simple data attributes of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: Dictionary representation of the object's attributes suitable for JSON.
    """
    # vars(obj) retourne un dictionnaire de tous les attributs de l'instance
    return vars(obj)
