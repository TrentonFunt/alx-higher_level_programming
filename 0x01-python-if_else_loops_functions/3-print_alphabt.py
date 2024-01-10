#!/usr/bin/python3
for alphabets in range(97, 123):
    if chr(alphabets) not in 'qe':
        print("{}".format(chr(alphabets)), end="")
