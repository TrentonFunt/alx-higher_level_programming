#!/usr/bin/python3
"""
Contains append_write function
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and
    return the number of characters added.

    Args:
        filename (str): The path to the file to be appended
        text (str): The string to be appended to the file

    Returns:
        int: The number of characters added to the file.
    """
    num_characters_added = 0

    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)

    return num_characters_added
