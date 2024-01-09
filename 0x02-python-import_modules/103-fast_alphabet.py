#!/usr/bin/python3
characters = map(chr, range(ord('A'), ord('Z') + 1))
print(*characters, sep='', end='\n')
