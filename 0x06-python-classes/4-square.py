#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    Square class that defines a square.

    Private instance attribute:
        - size: the size of the square

    Public instance methods:
        - def area(self): returns the current square area

    Properties:
        - def size(self): to retrieve the size attribute
        - def size(self, value): to set the size attribute

    Instantiation:
        __init__(self, size=0)

    Raises:
        - TypeError: if size is not an integer
        - ValueError: if size is less than 0
    """
    def __init__(self, size=0):
        """
        Initializes a new private instance of the Square class.

        Args:
            size (int): the size of the square (default: 0)
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): the size of the square.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
