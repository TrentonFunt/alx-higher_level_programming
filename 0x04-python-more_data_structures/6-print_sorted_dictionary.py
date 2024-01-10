#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Sort the keys and assign value
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate through the sorted keys and print the key pairs
    for key in sorted_keys:
        pair_key = a_dictionary[key]
        print(f"{key}: {pair_key}")
