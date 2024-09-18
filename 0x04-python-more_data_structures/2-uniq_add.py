#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_values = set()
    for num in my_list:
        unique_values.add(num)
    result = sum(unique_values)
    return result
