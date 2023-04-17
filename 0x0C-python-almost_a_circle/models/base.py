#!/usr/bin/python3
'''Module calss Base'''


class Base:
    '''
    Base class for other classes and sets up a private class attribute
    for counting the number of objects and a constructor for initializing
    instance ID values.

    Attributes:
        __nb_objects (int): The number of objects created for a class.
        id (int): The ID of an instance of a class.

    Methods:
        __init__(id=None): Constructor for initializing the instance ID values.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Constructor for initializing the instance id values.

        Args:
            id (int): An optional ID value for an instance.

        Returns:
            None.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
