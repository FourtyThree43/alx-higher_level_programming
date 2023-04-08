#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_docstring(self):  # tests docstr exists
        self.assertIsNotNone(max_integer.__doc__)

    def test_max_integer_all(self):
        """Test max_integer function with various input lists"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2.5, 3.7, 1.9, 6.1]), 6.1)
        self.assertRaises(TypeError, max_integer, [1, '2', 3])
        self.assertRaises(TypeError, max_integer, None)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([5, 2, 1, 4, 3]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-3, -2, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-3, 0, 5, -1]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.5]), 2.7)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3])
