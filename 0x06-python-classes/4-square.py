#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Class Square

    Attributes:
        __size (int): size the square
    """

    def __init__(self, size=0):
        """Method __init initialize a private instance

        Args:
            size (int): size the square
        Return: None
        """
        self.size = size

    def area(self):
        """calculates square's area
        Return:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size initialize a instance

        Args:
            value (int): size the square
        Return: None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
