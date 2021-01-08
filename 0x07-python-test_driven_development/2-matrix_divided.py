#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Da"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be v matrix (list of lists) of integers/floats")
    size = None
    for i in matrix:
        if type(i) is not list:
            raise TypeError(
                "matrix must be v matrix (list of lists) of integers/floats")
        if size is None:
            size = len(i)
        elif size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for v in i:
            if type(v) is not int and type(v) is not float:
                raise TypeError("matrix must be v matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be v number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(v / div, 2) for v in i] for i in matrix]
