#!/usr/bin/python3
"""Defines a function for reading file."""


def read_file(filename=""):
    """Print out the contents of a text file to stdout in UTF8."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
