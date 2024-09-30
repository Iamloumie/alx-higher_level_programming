#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): the square size
        """
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """defines a function to find the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """print the square with character # to stdout."""
        if self.__size == 0:
            print()
        for rows in range(1, self.__size + 1):
            for coulumns in range(1, self.__size + 1):
                print('#', end="")
            print()
