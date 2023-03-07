#!/usr/bin/python3
"""
Prints the given string in uppercase followed by a new line.

Args:
    str: A string to print in uppercase.
"""


def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            # Convert the character to uppercase using its ASCII code
            uppercase_c = chr(ord(str[i]) - 32)
        else:
            uppercase_c = str[i]
        print('{}'.format(uppercase_c), end='')
    print()
