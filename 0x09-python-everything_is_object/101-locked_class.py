#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    A class that prevents the user from dynamically creating
    new instance attributes, except for an attribute called 'first_name'.
    """
    __slots__ = ['first_name']

    def __init__(self):
        """Initialize the instance with a 'first_name' attribute."""
        self.first_name = None

    def __setattr__(self, key, value):
        """
        Called when an instance attribute is set.
        Raises an AttributeError if the attribute being set is not
        'first_name' and it does not already exist.
        """
        if key != 'first_name' and not hasattr(self, 'first_name'):
            raise AttributeError(f"'LockedClass' object has no attribute\
                                 '{key}'")
        super().__setattr__(key, value)
