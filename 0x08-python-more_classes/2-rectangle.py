#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle
        Args:
            width (int): The width of the newly created rectangle.
            height(int): The height of the newly created rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Finds the area of a rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Find the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
