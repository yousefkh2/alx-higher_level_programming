#!/usr/bin/python3
"""Module for rectangle setter and getter"""


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
