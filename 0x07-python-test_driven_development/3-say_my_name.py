#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>."

    Parameters:
    - first_name (str): The first name.
    - last_name (str): The last name. Default is an empty string.
    """
    # Check if first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the message
    print("My name is {} {}".format(first_name, last_name))

# Example usage:
say_my_name("John", "Doe")
