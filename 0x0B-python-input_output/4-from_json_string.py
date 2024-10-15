#!/usr/bin/python3
"""This module converts an oj into
its json representation"""
import json


def to_json_string(my_str):
    """
    This function Convert a Python object to its JSON representation.

    Args:
        my_str: the object to convert
    """
    return json.loads(my_str)
