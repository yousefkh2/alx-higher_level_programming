#!/usr/bin/python3
"""Rectangle that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Rectangle is an instance of Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def check_value(self, name, value, is_positive=True):
        """Check value for width, height, x, y"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if is_positive and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if not is_positive and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        return (value)

    @property
    def width(self):
        """Get the width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the width."""
        self.__width = self.check_value("width", value)

    @property
    def height(self):
        """Get the height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the height."""
        self.__height = self.check_value("height", value)

    @property
    def x(self):
        """Get x."""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set x."""
        self.__x = self.check_value("x", value, False)

    @property
    def y(self):
        """Get y."""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set y."""
        self.__y = self.check_value("y", value, False)

    def area(self):
        """Calculate the area of the rectangle."""
        return (self.width * self.height)

    def display(self):
        """Display to the stdout."""
        print("\n" * self.y, end="")
        print("\n".join([" " * self.x + "#" * self.width for _ in range(self.height)]))

    def __str__(self):
        """String representation of the Rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height))

    def update(self, *args, **kwargs):
        """Update the attributes."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return ({'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y})
