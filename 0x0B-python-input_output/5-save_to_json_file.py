#!/usr/bin/python3
"""writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write a Python object to a text file using JSON representation.

    Parameters:
        my_obj: Python object
        filename (str): Name of the file to save the JSON representation to
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
