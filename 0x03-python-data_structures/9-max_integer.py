#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_no = my_list[0]
    for i in my_list:
        if i > max_no:
            max_no = i

    return max_no
