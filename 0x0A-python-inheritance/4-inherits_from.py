#!/usr/bin/python3


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of
    a class that inherited from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a class
        that inherited from the specified class, False otherwise.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
