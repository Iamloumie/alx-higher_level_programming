#!/usr/bin/python3


def lookup(obj):
    """
    Return a list of valid attributes for the given object.

    This function uses the built-in dir() function to get a list of
    valid attributes for the provided object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list of strings representing valid attributes for the object.
    """
    return dir(obj)
