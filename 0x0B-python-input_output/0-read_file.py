#!/usr/bin/python3
"""Funtion read_file"""


def read_file(filename=""):
    """function that reads a text file (UTF8)"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
