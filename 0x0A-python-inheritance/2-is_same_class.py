#!/usr/bin/python3

"""Module to check if an obj is an instance of
a class
"""


def is_same_class(obj, a_class):
    """This checks if obj is an instance of
    a_class

    Args:
        obj: the object to check
        a_class: the class to check against
    """
    return type(obj) is a_class
