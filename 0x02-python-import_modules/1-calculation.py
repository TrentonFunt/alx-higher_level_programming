#!/usr/bin/python3
# import modules
from calculator_1 import add, sub, mul, div

# define arguments
a = 10
b = 5

# print result of calculator
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} + {} = {}".format(a, b, sub(a, b)))
print("{} + {} = {}".format(a, b, mul(a, b)))
print("{} + {} = {}".format(a, b, div(a, b)))
