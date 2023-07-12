#!/usr/bin/python3
"""Defines a  class"""


class Student:
    """Represent a student
    Args:
        first_name(str)
        last_name(str)
        age(int)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of
        class student"""

        return self.__dict__
