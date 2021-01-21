#!/usr/bin/python3
"""Function pascal_triangle"""


def pascal_triangle(n):
    """Representation pascal_triangle"""
    if n <= 0:
        return ([])

    trian = [[1]]
    for i in range(1, n):
        row = [1]
        temp = trian[i - 1]
        for j in range(len(temp)):
            pascal = temp[j] + temp[j + 1] if j != len(temp) - 1 else 1
            row.append(pascal)

        trian.append(row)

    return trian
