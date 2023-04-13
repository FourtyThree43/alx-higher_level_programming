#!/usr/bin/python3
'''Module class BaseGeometry'''


class BaseGeometry:
    '''empty class BaseGeometry'''
    pass

    def area(self) -> str:
        """Raises an Exception with the message: area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value) -> int | str | None:
        """
        Validates value and raises appropriate exceptions if necessary.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
