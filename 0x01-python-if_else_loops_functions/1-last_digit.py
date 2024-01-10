#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
zero_digit = abs(number) % 10
if number < 0:
    zero_digit = -zero_digit
print(f"Last digit of {number:d} is {zero_digit:d} and is ", end="")
if zero_digit > 5:
    print("greater than 5")
elif zero_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
