#!/usr/bin/python3
'''module to add integers'''


def add_integer(a, b=98) -> int | float:
    """
    add two integersa + b

    Args:
        a (int, float): the first integer to add
        b (int, float): the second integer to add,. Defaults to 98.

    Raises:
        TypeError:  if a or b are not integers or floats

    Returns:
        int: the addition of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
