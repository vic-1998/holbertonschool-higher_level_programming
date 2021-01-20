#!/usr/bin/python3
"""Class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation a rectangle"""

    def __init__(self, width, height):
        """
        Inicialize a Rectangle

        Args:
            width (int): retangle width
            height (int): retangle height
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
