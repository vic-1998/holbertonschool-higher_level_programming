#!/usr/bin/python3
"""Define Square class whith the __init__ funtion"""


class Square:
    """Class Square

    Attributes:
        __size (int): size the square
    """

    def __init__(self, size):
        """Method __init initialize a private instance

        Args:
            size (int): size the square
        Return: None
        """

        self.__size = size
