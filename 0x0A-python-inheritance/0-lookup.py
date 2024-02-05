#!/usr/bin/python3


def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of attributes and methods.
    """
    return [attr for attr in dir(obj)
            if not callable(getattr(obj, attr)) or not attr.startswith("__")]
