#!/usr/bin/python3
"""Creates a child class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a child class.
    Args:
        width(int)
        height(int)
    """

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Prints retangle description"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
