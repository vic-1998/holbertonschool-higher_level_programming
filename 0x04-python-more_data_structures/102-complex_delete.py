#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for array in list(a_dictionary):
        if a_dictionary[array] == value:
            del a_dictionary[array]
    return a_dictionary
