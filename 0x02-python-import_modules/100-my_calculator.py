#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # Extracting arguments
    a, operator, b = int(argv[1]), argv[2], int(argv[3])

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
        exit(1)

    # Result format
    print("{} {} {} = {}".format(a, operator, b, result))
