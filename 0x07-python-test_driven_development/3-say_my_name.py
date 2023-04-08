#!/usr/bin/python3
""" function that prints a string """


def say_my_name(first_name, last_name=""):
    '''
    Prints "My name is <first name> <last name>"

    Args:
        first_name (str): the first name to be printed
        last_name (str): the last name to be printed, defaults to empty string

    Raises:
        TypeError: if first_name or last_name is not a string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
