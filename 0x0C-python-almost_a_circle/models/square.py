#!/usr/bin/python3
"""
Module contains the class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Rectangle inherits from Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of the rectangle"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """updates attributes"""
        attri = ["id", "size", "x", "y"]
        if args is not None and args is not ():
            for index, var in enumerate(args):
                if index == 0:
                    self.id = var
                if index == 1:
                    self.size = var
                if index == 2:
                    self.x = var
                if index == 3:
                    self.y = var
        """kwargs argument"""
        if kwargs is not None and kwargs is not ():
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary of a Square"""
        r = {}
        r["id"] = self.id
        r["size"] = self.size
        r["x"] = self.x
        r["y"] = self.y
        return r
