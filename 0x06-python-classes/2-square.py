#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square with a a private attribute, size."""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.
        Args:
           size: The size of the square (int).
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
