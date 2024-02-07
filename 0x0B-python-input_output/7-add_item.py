#!/usr/bin/python3
"""
Contains module for add arguments
"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_arguments_to_list():
    """
    Adds all command-line arguments to a Python list
    and saves them to a file as a JSON representation.
    """
    # Load existing data from the file if it exists
    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []
    except json.JSONDecodeError:
        existing_data = []

    # Add new arguments to the list
    for arg in sys.argv[1:]:
        existing_data.append(arg)

    # Save the updated list to the file
    save_to_json_file(existing_data, "add_item.json")

if __name__ == "__main__":
    add_arguments_to_list()
