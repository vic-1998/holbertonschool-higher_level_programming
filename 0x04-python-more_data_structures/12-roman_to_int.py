#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)
    data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    r = roman_string
    list_data = [data[i[0]] if data[i[0]] >= data[i[1]] else (-1*data[i[0]])
                 for i in zip(r, r[1:] + r[-1])]
    res = sum(list_data)
    return (res)
