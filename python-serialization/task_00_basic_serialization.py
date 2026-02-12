#!/usr/bin/env python3
"""
task_00_basic_serialization.py

This module provides basic serialization and deserialization functions
for Python dictionaries using JSON format.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the JSON file to save the data.

    If the file already exists, it will be replaced.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dictionary")
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
