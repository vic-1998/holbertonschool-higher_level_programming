#!/usr/bin/python3

"""
Base modular tests
"""

from models.base import Base
import unittest
import pycodestyle
import inspect
import pep8
import json


class BaseTest(unittest.TestCase):
    """Set of tests"""

    @classmethod
    def setUpClass(cls):
        """a"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def setUp(self):
        """setting up for each test """
        Base._Base__nb_objects = 0

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_base.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_base(self):
        """Test models/base.py PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_positive_id(self):
        """A"""
        base = Base(16)
        self.assertEqual(base.id, 16)
        base = Base(22)
        self.assertEqual(base.id, 22)

    def test_negative_id(self):
        """A"""
        base = Base(-16)
        self.assertEqual(base.id, -16)
        base = Base(-22)
        self.assertEqual(base.id, -22)

    def tets_none_id(self):
        """a"""
        base = Base()
        self.assertEqual(base.id, 1)
        base = Base()
        self.assertEqual(base.id, 2)

    def test_docstring(self):
        """a"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_to_json_string(self):
        """a"""
        Base._Base__nb_objects = 0
        line1 = {"id": 2, "width": 5, "height": 6, "x": 7, "y": 8}
        line2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([line1, line2])
        self.assertTrue(type(json_s) is str)
        line = json.loads(json_s)
        self.assertEqual(line, [line1, line2])

    def test_emty_to_json_string(self):
        """a"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Tests regular from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_fjs_empty(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(""))

    def test_fjs_None(self):
        """Tests from_json_string th an empty string"""
        self.assertEqual([], Base.from_json_string(None))
