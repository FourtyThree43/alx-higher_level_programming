#!/usr/bin/python3
'''
    A module that define a Rectangle class.
'''


class Rectangle:
    '''
    A Recatangle class that define a rectangle.

    Private instance attribute:
        - width: the long-ness of the rectangle.
        - height: the tall-ness of the rectangle.

    Public instance methods:
        - def area(self): returns the current rectangle area
        - def perimeter(self): returns the current rectangle perimeter

    Properties:
        - def width(self): to retrieve the width attribute
        - def width(self, value): to set the width attribute

        - def height(self): to retrieve the height attribute
        - def height(self, value): to set the height attribute

    Instantiation:
        __init__(self, width=0, height=0)

    Args:
         - width (int): The length of the retangle.(default: 0)
         - height (int): The height of the rectaangle.(default: 0)

    Raises:
          - TypeError: width & height must be an integer.
          - ValueError: width & height must be >= 0
    '''

    def __init__(self, width=0, height=0) -> None:
        '''
            Initializes a new private instance of the Rectangle class.
        '''
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        '''
        Retrieves the width of the rectangle.

        Returns:
            The width of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        '''
        Sets the width of the rectangle.

        Args:
            value (int): the width of the rectangle.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must an intager")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        '''
        Retrieves the height of the rectangle.

        Returns:
            The height of the rectangle.
        '''
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        '''
        Sets the hight of the rectangle.

        Args:
            value (int): the height of the rectangle.

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("height must an intager")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self) -> int:
        """
        Computes the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self) -> int:
        """
        Computes the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self) -> str:
        '''
        Returns a string representation of the Rectangle object with "#" char.
        If the width or height of the rectangle is 0, return an empty string.

        Returns:
        str: a string representation of the rectangle.
        '''
        rec_string = ""
        if self.__width == 0 or self.__height == 0:
            return rec_string
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    rec_string += "#"
                rec_string += "\n"
            return rec_string[:-1]

    def __repr__(self) -> str:
        return "Rectangle({}, {})".format(self.__width, self.__height)

    '''
    def __del__(self) -> None:
        print("Bye rectangle...", flush=True)
    '''
