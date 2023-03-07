#!/usr/bin/python3
"""
Prints the given string in uppercase followed by a new line.
Convert ASCII to uppercase is c -32 i.e (a - 32) = A.
Args:
    str: A string to print in uppercase.
"""


def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            uppercase_c = chr(ord(str[i]) - 32)
        else:
            uppercase_c = str[i]
        print('{}'.format(uppercase_c), end='')
    print()
