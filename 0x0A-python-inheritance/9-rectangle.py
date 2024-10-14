#!/usr/bin/python3
"""Defines a base geometry class baseGeometry."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Inherited from Basegeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """print"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
