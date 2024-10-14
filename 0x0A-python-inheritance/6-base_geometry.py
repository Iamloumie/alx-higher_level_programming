#!/usr/bin/python3

class BaseGeometry:
    """
    A base class representing basic geometry.

    This class is intended to be subclassed by specific geometric shapes.
    It provides a placeholder method for calculating area.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        This method is meant to be overridden by subclasses.

        Raises:
            Exception: Always raises an exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")
