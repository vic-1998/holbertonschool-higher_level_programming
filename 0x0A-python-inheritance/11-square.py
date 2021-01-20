#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """class intance methos area"""

    def area(self):
        """return area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """representation a rectangle"""

    def __init__(self, width, height):
        """intance the rectangel"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """representation a square"""

    def __init__(self, size):
        """instance the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return area"""
        return self.__size ** 2

    def __str__(self):
        """string representation"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
