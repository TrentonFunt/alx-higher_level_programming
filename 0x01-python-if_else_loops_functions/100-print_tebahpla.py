#!/usr/bin/python3

for c in range(ord('z'), ord('A') - 1, -1):
    print("{:c}".format(c if (c - ord('A')) % 2 == 0 else c + 32), end="")

print()
