#!/usr/bin/python3
def remove_char_at(str, n):
    dele = ""
    i = 0
    for j in str:
        if (i != n):
            dele = dele + j
        i = i + 1
    return(dele)
