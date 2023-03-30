#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    Square class that defines a square.

    Private instance attribute:
        - size: the size of the square

    Instantiation:
        __init__(self, size=0)

    """

    def __init__(self, size):
        """
        Initializes a new private instance of the Square class.

        Args:
            size: the size of the square.
        """
        self.__size = size
