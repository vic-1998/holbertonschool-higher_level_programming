#!/usr/bin/python3
"""
Module contains the class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get of width"""
        return self.__width

    @property
    def height(self):
        """get of height"""
        return self.__height

    @property
    def x(self):
        """get of x"""
        return self.__x

    @property
    def y(self):
        """get of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """print a display"""
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def __str__(self):
        """string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """updates attributes"""
        attri = ["id", "widht", "height", "x", "y"]
        if args is not None and args is not ():
            for index, var in enumerate(args):
                if index == 0:
                    self.id = var
                if index == 1:
                    self.width = var
                if index == 2:
                    self.height = var
                if index == 3:
                    self.x = var
                if index == 4:
                    self.y = var
        """kwargs argument"""
        if kwargs is not None and kwargs is not ():
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary of a Rectangle"""
        r = {}
        r["id"] = self.id
        r["width"] = self.width
        r["height"] = self.height
        r["x"] = self.x
        r["y"] = self.y
        return r
