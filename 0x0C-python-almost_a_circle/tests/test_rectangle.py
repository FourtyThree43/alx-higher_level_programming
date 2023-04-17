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
