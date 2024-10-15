#!/usr/bin/python3

"""This module converts an obj into its json
representation
"""

import json


def from_json_string(my_str):
    """This function converts an obj into json

    Args:
        my_obj: the object to convert
    """
    return json.loads(my_str)
