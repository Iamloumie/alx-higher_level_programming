#!/usr/bin/python3

"""This module checks if an obj is an instance
of a class
"""


def is_kind_of_class(obj, a_class):
    """This compares if they inherit the same
    base class

    Args:
        obj: the obj to compare
        a_class: the class to compare with
    """
    return isinstance(obj, a_class)
