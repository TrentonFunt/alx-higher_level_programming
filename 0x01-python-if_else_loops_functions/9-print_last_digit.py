#!/usr/bin/python3
def print_last_digit(number):
    zero_digit = abs(number) % 10
    print(zero_digit, end="")
    return zero_digit
