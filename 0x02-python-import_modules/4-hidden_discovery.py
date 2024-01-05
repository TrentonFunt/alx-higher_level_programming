#!/usr/bin/python3

import hidden_4

if _name_ == "_main_":

    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter names based on conditions
    filtered_names = [name for name in names if not name.startswith('__')]

    # Sort the filtered names alphabetically
    sorted_names = sorted(filtered_names)

    # Print each name on a new line
    for name in sorted_names:
        print(name)
