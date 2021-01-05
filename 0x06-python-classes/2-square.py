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

        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
