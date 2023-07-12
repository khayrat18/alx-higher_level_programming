#!/usr/bin/python3
"""Checks instance of a class"""

def inherits_from(obj, a_class):
    """Checks if an objectn is exactly an instance
    of a class it inherited from directly or indirectly
    args:
        obj:
        a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
