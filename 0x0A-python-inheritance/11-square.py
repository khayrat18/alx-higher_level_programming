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
        self.integer_validator("size", size)

    def area(self):
        """Returns area."""
        return self.__size ** 2

    def __str__(self):
        """Prints square description"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
