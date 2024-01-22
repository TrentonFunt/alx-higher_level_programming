#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    printed_numbers = 0

    for i in range(x):
        try:
            # Print the element as an integer using "{:d}".format()
            print("{:d}".format(my_list[i]), end="")
            printed_numbers += 1
        except (ValueError, TypeError):
            # Ignore errors for non-integer elements
            pass

    print()  # Print a newline character after the integers
    return printed_numbers
