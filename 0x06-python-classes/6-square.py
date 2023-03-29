#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square with a a private attribute, size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new private instance: Size & Position
           of the Square class.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square to the given value."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Returns the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square to the given value."""
        if not isinstance(value, tuple) or len(value) != 2 \
           or not isinstance(value[0], int) or value[0] < 0 \
           or not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + '#' * self.__size)
