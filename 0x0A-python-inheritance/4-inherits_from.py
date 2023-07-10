#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Checks if an objectn is exactactly an instance
    of a class it inherited from directly or indirectly
    args:
        obj:
        a_class
    """
    return isinstance(obj, type) and issubclass(obj, a_class)
