#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        print("{}".format(chr(ord(char) - 32)
                         if ord(char) >= 97 and ord(char) <= 122 else char
        ), end="")
    print()
