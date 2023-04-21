#!/usr/bin/python3
'''Module for a Rectangle class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class inherits from the Rectangle class and
    sets up a square-shaped rectangle with sides of equal length.

    Attributes:
        size (int): The length of each side of the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
                        Constructor for initializing instance values.
        __str__(self): Returns a string representation of a Square instance.
        to_dictionary(self): Returns the dictionary representation of
                             a Square instance
    """

    def __init__(self, size, x=0, y=0, id=None) -> None:
        """
        Constructor for initializing instance values.

        Args:
            size (int): The length of each side of the square.
            x (int): The x-coordinate of the square's position (default 0).
            y (int): The y-coordinate of the square's position (default 0).
            id (int): The ID of an instance of this class (default None).

        Returns:
            None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """
        Returns:
            str: A string representation of the square,
            in the format "[Square] (<id>) <x>/<y> - <width>".
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self) -> int:
        """
        Gets the size of the square (equal to both width and height).

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value) -> None:
        """
        Sets the size of the square (equal to both width and height).

        Args:
            value (int): The new size of the square.

        Raises:
            ValueError: If the provided value is not a positive integer.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''
        Assigns an argument to each attribute.

        Args:
            args (ints):
                        1st argument is the id attribute
                        2nd argument is the size attribute
                        3rd argument is the x attribute
                        4th argument is the y attribute

            kwargs (dict): Optional keyword arguments.
                    Each key represents an attribute and its value represents
                    the value to be assigned to the attribute.
                    This type of argument is called a “key-worded argument”.
                    Argument order is not important.
        '''
        attrs = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        Returns the dictionary representation of  a Square instance

        Returns:
            A dictionary representing a Rectangle instance with these keys:
            - id
            - size
            - x
            - y
        '''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
