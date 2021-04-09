#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """Write a function that finds a peak"""
    x = list_of_integers
    l = len(x)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or x[m] >= x[m + 1]) and (m == 0 or x[m] >= x[m - 1]):
        return x[m]
    if m != l - 1 and x[m + 1] > x[m]:
        return find_peak(x[m + 1:])
    return find_peak(x[:m])
