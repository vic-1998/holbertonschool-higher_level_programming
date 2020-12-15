#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    cp_a = tuple_a + (0, 0)
    cp_b = tuple_b + (0, 0)
    copy = cp_a[0] + cp_b[0], cp_a[1] + cp_b[1],
    return copy
