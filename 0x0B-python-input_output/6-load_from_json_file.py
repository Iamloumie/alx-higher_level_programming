#!/usr/bin/python3
"""Creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file using JSON representation.

    Parameters:
        filename (str): Name of the file to save the JSON representation to
    """
    with open(filename, 'r', encoding="utf-8") as file:
        json.load(file)
