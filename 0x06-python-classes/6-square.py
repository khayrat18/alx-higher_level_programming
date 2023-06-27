#!/usr/bin/python3
"""Defines a class of square."""


class Square:
    """Represents a new square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square object
        Args:
            size (int),
            position (int,int)
        """
        self.__size = 0
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves a current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves current position square object"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(1, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with chaacter #."""
        if self.__size == 0:
            print("")
            return
        [print("")for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="")for j in range(0, self.__position[0])]
            [print("#", end="")for k in range(0, self.__size)]
            print("")
