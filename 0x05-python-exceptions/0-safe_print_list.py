#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_elements = 0

    try:
        # Iterate through the elements of the list
        for i in range(x):
            # Try to print the element
            print(my_list[i], end="")
            printed_elements += 1

    except IndexError:
        # Handle the IndexError if length of x is more than my_list
        pass

    finally:
        # Print a newline character after the elements
        print()

    return printed_elements
