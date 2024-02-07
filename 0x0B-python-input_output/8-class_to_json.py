#!/usr/bin/python3
"""
Contains module for class to json
"""


def class_to_json(obj):
    """Converts a Python class instance to a
    dictionary representation.
    """
    return obj.__dict__
