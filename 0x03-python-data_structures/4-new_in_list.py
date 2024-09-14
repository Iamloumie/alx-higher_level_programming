#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_length = len(my_list)
    copy = my_list.copy()

    if idx < 0 or idx >= list_length:
        return my_list
    copy[idx] = element
    return copy
