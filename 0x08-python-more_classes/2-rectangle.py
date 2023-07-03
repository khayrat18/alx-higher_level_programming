#!/usr/bin/python3

"""A class that defines a rectangle"""


class Rectangle:
    """Initializes rectangle object
    """

    def __init__(self, width=0, height=0):
        """creates instance of an object
        Args:
            width(int)
            height(int)
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves an attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets an attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves an attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets an attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """ Returns area of a rectangle"""
        return (self.width*self.height)

    def perimeter(self):
        """Return perimeter of a rectangle"""
        perimeter = 0
        return (2*(self.height + self.width))
