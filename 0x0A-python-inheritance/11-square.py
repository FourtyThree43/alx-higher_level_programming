#!/usr/bin/python3
'''Module class Square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class inherits from Rectangle and represents a square.
    """
    def __init__(self, size) -> None:
        """
        Intialize a new Square.

        Args:
            size(int): The sides of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self) -> str:
        """returns string representation of Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
