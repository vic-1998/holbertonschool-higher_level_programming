#!/usr/bin/python3
"""Funtion is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance or
    inherited from class, otherwise False."""
    return (isinstance(obj, a_class))
