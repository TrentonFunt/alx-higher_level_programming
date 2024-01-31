#!/usr/bin/python3


def print_square(size):
    """
    Prints a square with the character #.

    Parameters:
    - size (int): The size length of the square.
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is non-negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is an integer (not a float)
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square
    for i in range(size):
        print("#" * size)
