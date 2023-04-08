#!/usr/bin/python3
'''Moduel to print a square'''


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): the size length of the square.

    Raises:
        TypeError: if size is not an integer or float.
        ValueError: if size is less than 0.
        TypeError: if size is a float and is less than 0.

    Returns:
        None
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if isinstance(size, float):
        size = int(size)

    for i in range(size):
        print("#" * size)
