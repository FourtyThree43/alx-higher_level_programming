#!/usr/bin/python3
'''Module for a Rectangle class'''
from base import Base


class Rectangle(Base):
    '''
    The Rectangle class inherits from the Base class and
    sets up private instance attributes with public getter and
    setter methods. It also provides a constructor
    for initializing instance values.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle's position.
        __y (int): The y-coordinate of the rectangle's position.
        id (int): The ID of an instance of this class.

    Methods:
        width(self): Returns the current width value.
        width(self, value): Sets the value for width.
        height(self): Returns the current height value.
        height(self, value): Sets the value for height.
        x(self): Returns the current x-coordinate value.
        x(self, value): Sets the value for x-coordinate.
        y(self): Returns the current y-coordinate value.
        y(self, value): Sets the value for y-coordinate.
        __init__(self, width, height, x=0, y=0, id=None): Constructor for
            initializing instance values.
    '''

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        '''
        Constructor for initializing instance values.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position (default 0).
            y (int): The y-coordinate of the rectangle's position (default 0).
            id (int): The ID of an instance of this class (default None).

        Returns:
            None.
        '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''Returns the current width value'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the value for width.'''
        self.__width = value

    @property
    def height(self):
        '''Returns the current height value.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the value for height.'''
        self.__height = value

    @property
    def x(self):
        ''' Returns the current x-coordinate value.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Sets the value for x-coordinate.'''
        self.__x = value

    @property
    def y(self):
        '''Returns the current y-coordinate value.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Sets the value for y-coordinate'''
        self.__x = value
