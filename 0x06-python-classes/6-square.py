#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """
    Square class that defines a square.

    Private instance attribute:
        - size: the size of the square

    Public instance methods:
        - def area(self): returns the current square area
        - def my_print(self): prints the square using "#" character

    Properties:
        - def size(self): to retrieve the size attribute
        - def size(self, value): to set the size attribute

    Instantiation:
        __init__(self, size=0)

    Raises:
        - TypeError: if size is not an integer
        - ValueError: if size is less than 0
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): the size of the square (default: 0)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): the position of the square.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 \
           or not isinstance(value[0], int) or value[0] < 0 \
           or not isinstance(value[1], int) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square to the standard output using "#" characters.
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0] + '#' * self.__size)
