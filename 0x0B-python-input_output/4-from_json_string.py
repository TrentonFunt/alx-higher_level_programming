#!/usr/bin/python3
"""
Module that contains from_json_string
"""
import json


def from_json_string(my_str):
    """
    Returns the Python data structure
    ccccccccccccccccccccrepresented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python data structure
        represented by the JSON string.
    """
    return json.loads(my_str)