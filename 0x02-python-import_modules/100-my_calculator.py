#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def my_calculator():
    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Extract arguments
    a, operator, b = sys.argv[1:]

    # Convert a and b to integers
    a, b = int(a), int(b)

    # Perform calculation based on the operator
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Print the result
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":
    my_calculator()
