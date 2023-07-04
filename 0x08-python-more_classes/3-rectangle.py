#!/usr/bin/python3
"""Rectangle class, adding area and perimeter"""

class Rectangle:
    """Adds one step to the rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setting width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be a positive number")
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return (self.__height)
    
    @height.setter
    def height(self, value):
        """setting height"""
        if not isinstance(value, int):
            raise TypeError("Height has to be an integer")
        if value < 0:
            raise ValueError("Height must be a positive number")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)
    
    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.width + self.height * 2))
        
    def __str__(self):
        """print the rectangle with hashtags"""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        final = []
        for i in range(self.__height):
            [final.append('#') for j in range(self.__width)]
            if i != (self.__height - 1):
                final.append('\n')
        return ("".join(final))
