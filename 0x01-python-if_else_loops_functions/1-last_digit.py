#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
0_digit = abs(number) % 10
if number < 0:
    0_digit = -0_digit
print(f"Last digit of {number:d} is {0_digit:d} and is ", end="")
if 0_digit > 5:
    print("greater than 5")
elif 0_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
