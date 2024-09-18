#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    result = sum(a * b for a, b in my_list)
    div = sum(b for a, b in my_list)
    result = result / div

    return result
