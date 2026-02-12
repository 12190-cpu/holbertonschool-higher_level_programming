#!/usr/bin/python3
"""Script that adds all command line arguments to a list and saves them to add_item.json."""
import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

# Load the existing list from the file if it exists
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments (excluding the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
