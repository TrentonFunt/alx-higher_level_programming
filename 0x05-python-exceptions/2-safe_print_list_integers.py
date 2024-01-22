#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0

    try:
        # Iterate through the elements of the list
        for i in range(x):
            # Try to print the element as an integer using "{:d}".format()
            value = my_list[i]
            
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                printed_integers += 1

    except IndexError:
        # Raise IndexError if x is greater than the length of my_list
        raise

    finally:
        # Print a newline character after the integers
        print()

    return printed_integers
