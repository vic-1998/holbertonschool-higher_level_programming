#!/usr/bin/python3
"""Class Student"""


class Student:
    """Representation Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except:
                pass
        return new_dict
