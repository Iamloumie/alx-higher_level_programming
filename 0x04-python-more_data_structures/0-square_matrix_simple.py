#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_array = []
    for lists in matrix:
        result = list(map(lambda x: x ** 2, lists))
        new_array.append(result)
    return new_array
