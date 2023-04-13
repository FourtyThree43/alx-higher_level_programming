#!/usr/bin/python3
'''Module class BaseGeometry'''


class BaseGeometry:
    '''empty class BaseGeometry'''

    def area(self) -> str:
        """Raises an Exception with the message: area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
