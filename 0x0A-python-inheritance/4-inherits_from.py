#!/usr/bin/python3
"""Funtion inherits_from"""


def inherits_from(obj, a_class):
    """return True if object is a instance of class, otherwise False"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
