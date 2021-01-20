#!/usr/bin/python3
"""Class Student"""


class Student:
    """Representation Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary"""
        return self.__dict__
