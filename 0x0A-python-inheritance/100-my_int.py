#!/usr/bin/python3
"""
Class MyInt
"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """method"""
        return int(self) != other

    def __ne__(self, other):
        """method"""
        return int(self) == other
