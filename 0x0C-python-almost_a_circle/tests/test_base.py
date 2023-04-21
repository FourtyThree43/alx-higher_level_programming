#!/usr/bin/python3
'''Module for unittests for Rectangle class'''

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    '''Tests for Base class'''

    def test_init_no_id(self):
        '''Test __init__ with no ID'''
        b1 = Base()
        assert isinstance(b1, Base)
        assert hasattr(b1, 'id')
        '''assert b1.id == 1'''

        b2 = Base()
        assert isinstance(b2, Base)
        assert hasattr(b2, 'id')
        '''assert b2.id == 2'''


    def test_init_with_id(self):
        '''Test __init__ with ID'''
        b1 = Base(100)
        assert isinstance(b1, Base)
        assert hasattr(b1, 'id')
        assert b1.id == 100

        b2 = Base(200)
        assert isinstance(b2, Base)
        assert hasattr(b2, 'id')
        assert b2.id == 200

    def test_create(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r2 = Rectangle.create(**r_dict)
        self.assertEqual(str(r), str(r2))

    def test_to_json_string(self):
        # Test passing empty list to method
        empty_list = []
        empty_json = Base.to_json_string(empty_list)
        self.assertEqual(empty_json, "[]")

        # Test converting multiple Rectangle objects to JSON string
        r1 = Rectangle(4, 5, 6)
        r2 = Rectangle(1, 2)
        r_list = [r1, r2]
        r_json = Base.to_json_string([r.to_dictionary() for r in r_list])
        self.assertEqual(r_json, '[{"id": 8, "width": 4, "height": 5, "x": 6, "y": 0}, {"id": 9, "width": 1, "height": 2, "x": 0, "y": 0}]')

        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r_json = Base.to_json_string([r_dict])
        self.assertEqual(r_json, '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]')

    def test_from_json_string(self):
        # Test converting empty string to list
        empty_list = Base.from_json_string("[]")
        self.assertEqual(empty_list, [])

        # Test loading list of Rectangle objects from JSON string
        r_dict_list = [{"id": 8, "width": 4, "height": 5, "x": 6, "y": 0}, {"id": 9, "width": 1, "height": 2, "x": 0, "y": 0}]
        r_list = [Rectangle.create(**r_dict) for r_dict in r_dict_list]
        r_json = Base.to_json_string([r.to_dictionary() for r in r_list])
        loaded_list = Base.from_json_string

        r_json = '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
        obj_list = Base.from_json_string(r_json)
        self.assertEqual(len(obj_list), 1)

    def test_save_to_file(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}, {"id": 1, "width": 5, "height": 4, "x": 3, "y": 2}]')

    def test_load_from_file(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r, r2])
        obj_list = Rectangle.load_from_file()
        self.assertEqual(len(obj_list), 2)
