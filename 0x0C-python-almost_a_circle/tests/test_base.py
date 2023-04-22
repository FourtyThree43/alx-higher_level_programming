#!/usr/bin/python3
'''Module for unittests for Rectangle class'''

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    '''Tests for Base class'''

    def test_init_no_id(self):
        '''Test __init__ with no ID'''
        b1 = Base()
        assert isinstance(b1, Base)
        assert hasattr(b1, 'id')
        self.assertEqual (b1.id, 5)

        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b2.id, b3.id - 1)

        b4 = Base()
        b5 = Base()
        b6 = Base()
        self.assertEqual(b4.id, b6.id - 2)

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

        sq1 = Square(1, 2, 3, 4)
        sq_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq_dict)
        self.assertEqual(str(sq1), str(sq2))

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
        r_list_deserialized = json.loads(r_json)    # Deserialize the JSON string back into a list of dictionaries,
        r_json_reserialized = json.dumps(r_list_deserialized) # then reserialize the list and compare to the original JSON string.
        self.assertEqual(r_json, r_json_reserialized)

        sq1 = Square(4, 5, 6)
        sq2 = Square(1, 2)
        sq_list = [sq1, sq2]
        sq_json = Base.to_json_string([sq1.to_dictionary() for sq1 in sq_list])
        sq_list_deserialized = json.loads(sq_json)    # Deserialize the JSON string back into a list of dictionaries,
        sq_json_reserialized = json.dumps(sq_list_deserialized) # then reserialize the list and compare to the original JSON string.
        self.assertEqual(sq_json, sq_json_reserialized)

        r = Rectangle(1, 2, 3, 4, 5)
        r_dict = r.to_dictionary()
        r_json = Base.to_json_string([r_dict])
        self.assertEqual(r_json, '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]')

        sq1 = Square(1, 2, 3, 4)
        sq_dict = sq1.to_dictionary()
        sq_json = Base.to_json_string([sq_dict])
        sq_list_deserialized = json.loads(sq_json)    # Deserialize the JSON string back into a list of dictionaries,
        sq_json_reserialized = json.dumps(sq_list_deserialized) # then reserialize the list and compare to the original JSON string.
        self.assertEqual(sq_json, sq_json_reserialized)

    def test_from_json_string(self):
        # Test converting empty string to list
        empty_list = Base.from_json_string("[]")
        self.assertEqual(empty_list, [])

        # Test loading list of Rectangle objects from JSON string
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

        r_json = '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
        obj_list = Base.from_json_string(r_json)
        self.assertEqual(len(obj_list), 1)

    def test_save_to_file(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}, {"id": 1, "width": 5, "height": 4, "x": 3, "y": 2}]')

        s = Square(1, 2, 3, 4)
        s2 = Square(5, 4, 3, 2)
        Square.save_to_file([s, s2])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[{"id": 4, "size": 1, "x": 2, "y": 3}, {"id": 2, "size": 5, "x": 4, "y": 3}]')

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_load_from_file(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file([r, r2])
        obj_list = Rectangle.load_from_file()
        self.assertEqual(len(obj_list), 2)

        s = Square(1, 2, 3, 4)
        s2 = Square(5, 4, 3, 2)
        Square.save_to_file([s, s2])
        obj_list = Square.load_from_file()
        self.assertEqual(len(obj_list), 2)

class TestFromJsonString(unittest.TestCase):

    def test_list_output_type(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_output, list)

    def test_one_rectangle_output(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_two_rectangles_output(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_one_square_output(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_two_squares_output(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_None_input(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_empty_list_input(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_no_args_input(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_more_than_one_arg_input(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

import unittest

class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)

class TestBaseSaveToFile(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 77)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertEqual(len(f.read()), 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 39)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)
