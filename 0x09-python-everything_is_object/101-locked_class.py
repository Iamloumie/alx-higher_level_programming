#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes call 'first_name'.
    """
    __slots__ = ["first_name"]
