#!/usr/bin/python3
"""Class that inherits from a rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from rectangle
    Args:
        size(int)
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size