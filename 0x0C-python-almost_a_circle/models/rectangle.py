#!/usr/bin/python3

"""Module for a Rectangle building class"""

from models.base import Base


class Rectangle(Base):
    """Class to create a new Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor to create a new Rectangle

        Args:
            width: the width of the Rectangle
            height: the height of the Rectangle
            x: the x position of the Rectangle
            y: the y position of the Rectangle
            id: could be the instance of the class or
                what the user enters
        """
        self.__width = self.__validate_value("width", width, int, 1)
        self.__height = self.__validate_value("height", height, int, 1)
        self.__x = self.__validate_value("x", x, int)
        self.__y = self.__validate_value("y", y, int)
        super().__init__(id)

    # PROPERTY SETTERS AND GETTERS FOR VARIOUS ATTRIBUTES
    # BEGIN
    @property
    def width(self):
        """Getter method for the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method for the width"""
        self.__width = self.__validate_value("width", width, int, 1)

    @property
    def height(self):
        """Getter method for the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for the height"""
        self.__height = self.__validate_value("height", height, int, 1)

    @property
    def x(self):
        """Getter method for the x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter method for the x value"""
        self.__x = self.__validate_value("x", x, int)

    @property
    def y(self):
        """Getter method for the y value"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter method for the y value"""
        self.__y = self.__validate_value("y", y, int)

    # PROPERTY SETTERS AND GETTERS FOR VARIOUS ATTRIBUTES
    # END

    # HELPERS START
    def area(self):
        """This method returns the area of the Rectangle"""
        return self.__width * self.__height

    def update(self, *args, **kwargs):
        """This method updates attributes based on *args or **kwargs

        Args:
            args: Variable-length positional arguments
            kwargs: Variable-length keyword arguments
        """
        attributes = ['id', 'width', 'height', 'x', 'y']

        if args is not None and len(args) != 0:
            if len(args) > 5:
                raise IndexError("list index out of range")

            for i, value in enumerate(args):
                if not isinstance(value, int):
                    raise TypeError("{} must be an int".format(attributes[i]))
                setattr(self, attributes[i], value)
        elif kwargs and not args:
            for key, value in kwargs.items():
                if not isinstance(value, int):
                    raise TypeError("{} must be an int".format(key))
                setattr(self, key, value)

    def display(self):
        """Print the rectangle as a grid of #
        patterns
        """
        pattern = "\n" * self.__y
        for _ in range(self.__height):
            pattern += " " * self.__x
            pattern += "#" * self.__width + "\n"
        print("{}".format(pattern[:-1]))

    def __validate_value(self, name, value, Type, min=0):
        """This helper method validates incoming values for
        each method

        Args:
            name: this is the name of the value e.g x or y or height
            value: this the value coming in for validation
            Type: this is the expected type of the value
            min: this is the minimum expected value for the value

        Return:
            returns the value if it passes all Type and min checks
        """
        if not type(value) is Type:
            raise TypeError("{} must be an integer".format(name))
        if min == 0 and value < min:
            raise ValueError("{} must be >= 0".format(name))
        if min == 1 and value < min:
            raise ValueError("{} must be > 0".format(name))

        return value

    def to_dictionary(self):
        """This returns a dictionary representation of
        the Rectangle
        """
        dictionary = {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }

        return dictionary
    # HELPERS END

    def __str__(self):
        """This method returns the string representation of
        a Rectangle instance
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                  self.id, self.__x, self.__y, self.__width, self.__height
                  )
