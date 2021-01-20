#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """class public instance methods area"""

    def area(self):
        """raise an exception call"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
