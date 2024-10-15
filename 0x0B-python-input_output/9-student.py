#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new studeent.

        Args:
        first_name (str): Student's first name
        last_name (str): Student's last name
        age (int): student's age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the studedent."""
        return self.__dict__
