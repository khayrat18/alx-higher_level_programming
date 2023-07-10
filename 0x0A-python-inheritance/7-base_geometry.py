#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry:
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public method.
        Args:
            name:
            value:
        Returns: either a ValueError or TypeError
        """
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("{},must be an integer".format(name))
        if value <= 0:
            raise ValueError("{},must be greater than 0".format(name))
