#!/usr/bin/python3

"""Module for creating a square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class to create a new square that inherits
    from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the square class

        Args:
            size: the size of the square
            x: the x position of the square
            y: the y position of the square
            id: the instance id of the square
        """
        super().__init__(size, size, x, y, id)

    # GETTERS AND SETTERS BEGIN
    @property
    def size(self):
        """Getter method for the Square"""
        return super().width

    @size.setter
    def size(self, value):
        """Setter method for the Square"""
        self.width = value
        self.height = value
    # GETTERS AND SETTERS END

    def update(self, *args, **kwargs):
        """This method updates attributes based on *args or **kwargs

        Args:
            args: Variable-length positional arguments
            kwargs: Variable-length keyword arguments
        """
        attributes = ['id', 'size', 'x', 'y']

        if args is not None and len(args) != 0:
            if len(args) > 4:
                raise IndexError("list index out of range")
            for i, value in enumerate(args):
                if not isinstance(value, int):
                    raise TypeError("{} must be an int".format(attributes[i]))
                if attributes[i] != 'size':
                    setattr(self, attributes[i], value)
                else:
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
        elif kwargs and not args:
            for key, value in kwargs.items():
                if not isinstance(value, int):
                    raise TypeError("{} must be an int".format(key))
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """This returns a dictionary representation of
        the Rectangle
        """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

    def __str__(self):
        """This method returns the string representation of
        a Square instance
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.height)
