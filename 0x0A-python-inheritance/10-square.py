#!/usr/bin/python3
"""Class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation a square"""

    def __init__(self, size):
        """instance square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return area square"""
        return self.__size ** 2
