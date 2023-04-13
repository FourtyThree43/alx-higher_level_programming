#!/usr/bin/python3
'''Module add attribute'''


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (object): The object to add the new attribute to.
        attr (str): The name of the new attribute to add.
        value (any): The value of the new attribute.

    Raises:
        TypeError: If the object cannot have a new attribute added to it.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
