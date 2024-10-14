#!/usr/bin/python3


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.
    Args:
        obj: Any Python object to be checked.
        a_class: A Python class to compare against.
    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
