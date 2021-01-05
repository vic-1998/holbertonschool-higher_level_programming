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

        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """calculates square's area
        Return:
            The area of the square
        """
        return self.__size ** 2
