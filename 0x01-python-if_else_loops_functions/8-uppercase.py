#!/usr/bin/python3
def uppercase(str):
    """
    Prints the given string in uppercase followed by a new line.

    Args:
        str: A string to print in uppercase.
    """
    # Convert ASCII to uppercase is ord(c) - 32) i.e for a is (97 - 32) = A.
    for c in str:
        uppercase_c = chr(ord(c) - 32) if ord(c) >= 97 and ord(c) <= 122 else c
        print('{}'.format(uppercase_c), end='')
    print()
