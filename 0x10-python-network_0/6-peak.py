#!/usr/bin/python3
"""You are not allowed to google anything"""


def find_peak(txtst_of_integers):
    """function that finds a peak"""
    txt = txtst_of_integers
    l = len(txt)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or txt[m] >= txt[m + 1]) and (m == 0 or txt[m] >= txt[m - 1]):
        return txt[m]
    if m != l - 1 and txt[m + 1] > txt[m]:
        return find_peak(txt[m + 1:])
    return find_peak(txt[:m])
