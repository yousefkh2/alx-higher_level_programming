#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Subclass of Rectangle representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Represent Square instance as string."""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Get the size."""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set the size."""
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes."""
        attributes = ["id", "size", "x", "y"]
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return ({'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y})
