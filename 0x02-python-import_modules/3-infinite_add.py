#!/usr/bin/python3

import sys
if __name__ == "__main__":

    # Summing up all command-line arguments
    result = sum(int(arg) for arg in sys.argv[1:])

    # Printing the result followed by a new line
    print(result)
