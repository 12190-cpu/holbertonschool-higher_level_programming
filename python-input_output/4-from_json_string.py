#!/usr/bin/python3
"""Module that defines a function to convert a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The corresponding Python object (list, dict, etc.).
    """
    return json.loads(my_str)
