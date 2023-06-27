#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a new square"""
    def __init__(self, size=0):
        """Initialiazes a square object
        Args:
        Size (int)
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """Retrieves size of square"""
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
        return (self.size ** 2)

    def my_print(self):
        """Prints square  character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
