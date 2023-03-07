#!/usr/bin/python3
"""
    Checks whether the given character is lowercase.

    Args:
        c: A character to check.

    Returns:
        True if the character is lowercase, False otherwise.
    """
# ASCII code of the character codes for 'a' and 'z' is between 97 and 122


def islower(c):
    return (ord(c) >= 97 and ord(c) <= 122)
