#!/usr/bin/python3
"""
Class MyInt
"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    
