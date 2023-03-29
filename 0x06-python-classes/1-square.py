#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square with a private attribute, size."""

    def __init__(self, size):
        """Initializes a new instance of the Square class.
        Args:
           size: The size of the square.
        """
        self.__size = size
