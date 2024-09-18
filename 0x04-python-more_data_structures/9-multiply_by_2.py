#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for keys in new_dict:
        new_dict[keys] *= 2
    return new_dict
