#!/usr/bin/python3

"""Define  a square"""


def print_square(size):
    """Prints a square  with the cahracter #
    Args:
        int(size)
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
