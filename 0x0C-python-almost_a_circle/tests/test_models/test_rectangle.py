#!/usr/bin/python3
"""A"""

import unittest
import pep8
import json
import inspect
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangleDocs(unittest.TestCase):
    """a"""

    @classmethod
    def setUpClass(cls):
        """a"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_pep8_rectangle(self):
        """A"""
        pep8style = pep8.StyleGuide(quier=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style eeros (and warnings).")

    def test_pep8_test(self):
        """a"""
        pep8style = pep8.StyleGuide(quier=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style eeros (and warnings).")


class TestRectangle(unittest.TestCase):
    """a"""

    @classmethod
    def setUpClass(cls):
        """a"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(5, 6, 7, 8, 9)
        cls.r4 = Rectangle(11, 12, 13, 14)

    def test_id(self):
        """a"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 9)
        self.assertEqual(self.r4.id, 3)
