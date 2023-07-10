#!/usr/bin/python3
"""Defines an object"""


def is_kind_of_class(obj, a_class):
    """Checks if an objectn is exactactly an instance
    of a class it inherited from
    args:
        obj:
        a_class
    """
    return isinstance(obj, a_class) or type(obj) == a_class
