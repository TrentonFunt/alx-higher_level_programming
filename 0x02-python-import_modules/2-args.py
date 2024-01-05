#!/usr/bin/python3

import sys
if _name_ == "_main_":

    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    print("{} {}{}".format(
        num_args,
        "argument" if num_args == 1 else "arguments",
        ":" if num_args > 0 else "."
       ))

    # Print the arguments and their positions
    for i in range(1, num_args + 1):
        print("{}: {}".format(i, sys.argv[i]))
