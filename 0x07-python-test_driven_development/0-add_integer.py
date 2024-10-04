#!/usr/bin/python3
"""Defines an integer addition functions"""


def add_integer(a, b=98):
    """Returns the sum of a and b

    float argument are typecasted to int before they are printed

    Raises:
        TypeErrorif either a or b is a non integer
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
