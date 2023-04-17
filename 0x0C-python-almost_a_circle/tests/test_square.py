#!/usr/bin/python3
'''Module for unittests for Square class'''

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_size(self):
        # Test getting and setting size
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(square.size, 10)

        # Test setting invalid size
        with self.assertRaises(ValueError):
            square.size = -5

    def test_area(self):
        # Test area calculation
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_str(self):
        # Test string representation
        square = Square(5, 1, 2, 3)
        self.assertEqual(str(square), "[Square] (3) 1/2 - 5")

    def test_update(self):
        # Test update method
        square = Square(5)
        square.update(1, 10, 2, 3)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 10")

        # Test update with kwargs
        square.update(y=4, x=5, size=20, id=2)
        self.assertEqual(str(square), "[Square] (2) 5/4 - 20")
