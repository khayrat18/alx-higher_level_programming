#!/usr/bin/python3
"""Defines a class"""


class MyList(list):
    """ A class MyList inherits of list"""

    def print_sorted(self):
        """Prints a list in ascending order"""
        print(sorted(self))
