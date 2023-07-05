#!/usr/bin/python3
""" Defines addition fuctions"""


def add_integer(a, b=98):
    """Return sum
    Args:
        int(a,b)
    Returns:
        sum
    Raises:
        TypeError: if neither a or b is an integer or float
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
