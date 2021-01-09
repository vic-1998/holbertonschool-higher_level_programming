#!/usr/bin/python3
"""
unittest module 6-max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Interactive tests"""
    def test_max(self):
        """Test max_integer """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([2, 3, 8]), 5)
        self.assertEqual(max_integer([1, -2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer(), None)


if __name__ == '__main__':
    unittest.main()
