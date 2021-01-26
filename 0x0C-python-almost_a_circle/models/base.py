#!/usr/bin/python3
"""
Module contains the class Base
"""

import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string"""
        filename = cls.__name__ + ".json"
        file = []
        if list_objs is not None:
            for i in list_objs:
                file.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(file))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of json"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return an empty list"""
        filename = cls.__name__ + ".json"
        lis = []
        try:
            with open(filename, 'r') as f:
                lis = cls.from_json_string(f.read())
            for i, val in enumerate(lis):
                lis[i] = cls.create(**lis[i])
        except:
            pass
        return lis
