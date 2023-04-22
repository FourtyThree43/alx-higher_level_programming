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

    def test_str(self):
        s = Square(2, 3, 4, 5)
        self.assertEqual(str(s), '[Square] (5) 3/4 - 2')

    def test_to_dictionary(self):
        '''Tests for to_dictionary method'''

        s = Square(2, 3, 4, 5)
        self.assertEqual(s.to_dictionary(), {'id': 5, 'size': 2, 'x': 3, 'y': 4})

        s1 = Square(10, 2, 1, 9)
        s1_dict = s1.to_dictionary()
        expected = {'id': 9, 'size': 10, 'x': 2, 'y': 1}
        self.assertDictEqual(s1_dict, expected)

        s2 = Square(5)
        s2_dict = s2.to_dictionary()
        expected = {'id': s2.id, 'size': 5, 'x': 0, 'y': 0}
        self.assertEqual(s2_dict, expected)

        s3 = Square(7, 3, 2)
        s3_dict = s3.to_dictionary()
        expected = {'id': s3.id, 'size': 7, 'x': 3, 'y': 2}
        self.assertDictEqual(s3_dict, expected)

        s4 = Square(2, 1, 1)
        s4_dict = s4.to_dictionary()
        expected = {'id': s4.id, 'size': 2, 'x': 1, 'y': 1}
        self.assertDictEqual(s4_dict, expected)

        s5 = Square(8, 5, 3, 10)
        s5_dict = s5.to_dictionary()
        expected = {'id': 10, 'size': 8, 'x': 5, 'y': 3}
        self.assertDictEqual(s5_dict, expected)
