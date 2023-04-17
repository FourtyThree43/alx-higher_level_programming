#!/usr/bin/python3
'''Module for unittests for Rectangle class'''

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    '''Tests for Base class'''

    def test_init_no_id(self):
        '''Test __init__ with no ID'''
        b1 = Base()
        assert isinstance(b1, Base)
        assert hasattr(b1, 'id')
        assert b1.id == 1

        b2 = Base()
        assert isinstance(b2, Base)
        assert hasattr(b2, 'id')
        assert b2.id == 2


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
