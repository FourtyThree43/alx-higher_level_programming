#!/usr/bin/python3
'''Module for unittests for Rectangle class'''

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Tests for Rectangle class'''
    def setUp(self):
        self.rect = Rectangle(5, 10)

    def test_width(self):
        '''Test width'''
        self.rect.width = 20
        self.assertEqual(self.rect.width, 20)
        with self.assertRaises(ValueError):
            self.rect.width = -1
        with self.assertRaises(TypeError):
            self.rect.width = "20"

    def test_height(self):
        '''Test height'''
        self.rect.height = 30
        self.assertEqual(self.rect.height, 30)
        with self.assertRaises(ValueError):
            self.rect.height = -1
        with self.assertRaises(TypeError):
            self.rect.height = "30"

    def test_x(self):
        '''Test x'''
        self.rect.x = 2
        self.assertEqual(self.rect.x, 2)
        with self.assertRaises(ValueError):
            self.rect.x = -1
        with self.assertRaises(TypeError):
            self.rect.x = "2"

    def test_y(self):
        '''Test y'''
        self.rect.y = 5
        self.assertEqual(self.rect.y, 5)
        with self.assertRaises(ValueError):
            self.rect.y = -1
        with self.assertRaises(TypeError):
            self.rect.y = "5"

    def test_area(self):
        '''Test area method'''
        self.assertEqual(self.rect.area(), 50)

    def test_display(self):
        '''Test display method'''
        print("")
        self.rect.display()  # should print a 5x10 rectangle of "#" characters

    def test_str(self):
        '''Test __str__ method'''
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), '[Rectangle] (12) 2/1 - 4/6')

    def test_update(self):
        '''Test update method'''
        self.rect.update(2, 10, 20, 30, 40)
        self.assertEqual(self.rect.id, 2)
        self.assertEqual(self.rect.width, 10)
        self.assertEqual(self.rect.height, 20)
        self.assertEqual(self.rect.x, 30)
        self.assertEqual(self.rect.y, 40)

    def test_to_dictionary(self):
        '''Tests for to_dictionary method'''

        r1 = Rectangle(10, 20, 2, 4, 6)
        r1_dict = r1.to_dictionary()
        expected = {'id': 6, 'width': 10, 'height': 20, 'x': 2, 'y': 4}
        self.assertEqual(r1_dict, expected)

        '''test_to_dictionary_default_values'''
        r2 = Rectangle(1 ,1, 0, 0, 8)
        r2_dict = r2.to_dictionary()
        expected = {'id': 8, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        self.assertEqual(r2_dict, expected)

        '''test_to_dictionary_negative_value'''
        r3 = Rectangle(5, 5, -2, -3, 10)
        r3_dict = r3.to_dictionary()
        expected = {'id': 10, 'width': 5, 'height': 5, 'x': -2, 'y': -3}
        self.assertEqual(r3_dict, expected)

        '''test_to_dictionary_large_values'''
        r4 = Rectangle(999999999, 999999999, 999999999, 999999999, 999999999)
        r4_dict = r4.to_dictionary()
        expected = {'id': 999999999, 'width': 999999999, 'height': 999999999,
                    'x': 999999999, 'y': 999999999}
        self.assertEqual(r4_dict, expected)
