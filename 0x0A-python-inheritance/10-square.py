#!/usr/bin/python3

"""Square module that inherits from Base Geometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        """Class instantiation method

        Args:
            size: the size of the Sq
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size
