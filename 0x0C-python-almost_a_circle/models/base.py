#!/usr/bin/python3
'''Module calss Base'''
import json
import csv


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
        to_json_string(list_dictionaries):
    '''
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        '''
        Constructor for initializing the instance id values.

        Args:
            id (int): An optional ID value for an instance.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries) -> str:
        """Returns a JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            A JSON string representation of the list of dictionaries.
            If the input list is None or empty, returns the string "[]".

        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of Python dictionaries from a JSON string
        representation.

        Args:
            json_string (str): A string representing a list of dictionaries
                                in JSON format.

        Returns:
            A list of dictionaries. If the input string is None or empty,
            returns an empty list.

        """
        if json_string is None or json_string == '[]':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []
        object_list = cls.from_json_string(json_string)
        instance_list = [cls.create(**obj_dict) for obj_dict in object_list]
        return instance_list
