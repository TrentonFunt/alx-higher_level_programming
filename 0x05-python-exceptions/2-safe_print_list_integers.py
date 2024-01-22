#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        # Iterate through the elements of the list
        for i in range(x):
            # Check if the element is an integer before trying to format
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
            else:
                print("wrong type", end="")

    except IndexError:
        # Raise IndexError if x is greater than the length of my_list
        raise

    finally:
        # Print a newline character after the integers or error message
        print()

    return printed_integers
