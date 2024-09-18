#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for num in new_list:
        if num == search:
            index_replace = new_list.index(search)
            new_list[index_replace] = replace

    return new_list
