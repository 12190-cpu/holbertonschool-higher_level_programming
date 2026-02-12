#!/usr/bin/python3
"""Module that defines a function to write an object to a text file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file to write the JSON data into.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
