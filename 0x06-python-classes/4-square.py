#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """ Represents a square objec"""
    def __init__(self, size=0):
        """Initializes a square object
        Args:
            size (int)
        """
        self.size = size

    @property
    def size(self):
        """Retrieves size square object"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current square area"""
        return (self.__size * self.__size)
