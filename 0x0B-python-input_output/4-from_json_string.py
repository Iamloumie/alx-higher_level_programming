#!/usr/bin/python3
"""defines a string-to-JSON function."""
import json


def to_json_string(my_str):
    """
    Convert a Python object to its JSON representation.

    Parameters:
        my_obj: Python object

    Returns:
        str: JSON representation of the object
    """
    return json.loads(my_str)
