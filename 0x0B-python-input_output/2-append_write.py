#!/usr/bin/python3
"""Funtion append_write"""


def append_write(filename="", text=""):
    """returns the number of characters appended"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
