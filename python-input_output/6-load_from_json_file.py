#!/usr/bin/python3
"""Module that defines a function to create an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        object: The Python object represented by the JSON file content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
