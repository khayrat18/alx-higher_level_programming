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

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
