#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dicti = a_dictionary.copy()
    for keys, values in new_dicti.items():
        new_dicti[keys] = values * 2
    return new_dicti
