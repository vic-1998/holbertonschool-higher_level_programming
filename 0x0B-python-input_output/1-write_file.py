#!/usr/bin/python3
"""Funtion write_file"""


def write_file(filename="", text=""):
    """return the number of the characters written"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
