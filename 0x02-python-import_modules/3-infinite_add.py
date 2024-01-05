#!/usr/bin/python3

if _name_ == "_main_":

    import sys

    # Summing up all command-line arguments
    result = sum(int(arg) for arg in sys.argv[1:])

    # Printing the result followed by a new line
    print(result)
