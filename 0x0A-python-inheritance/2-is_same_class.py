#!/usr/bin/python3
"""Defines a class"""


def is_same_class(obj, a_class):
    """Checks if an object is exacly an instance
    of a class or not
    args:
        obj:
        a_class
    """
    if type(obj) == a_class:
        return True
    return False