#!/usr/bin/python3
"""Class MyList"""


class MyList(list):
    """subclass list"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """instance method and prints the sorted list"""
        print(sorted(self))
