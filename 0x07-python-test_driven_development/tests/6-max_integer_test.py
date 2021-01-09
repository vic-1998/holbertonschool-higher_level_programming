#!/usr/bin/python3
"""

"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """“Interactive tests”
    """

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer(), None)

    if __name__ == '__main__':
        unittest.main()
