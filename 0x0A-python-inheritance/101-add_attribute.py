#!/usr/bin/python3
"""Adds a new attribute to an object if possible"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.
    Raises a TypeError exception if the object can't have new attributes.
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
