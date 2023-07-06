#!/usr/bin/python3
"""Defines a function that prints first_name and last_name"""


def say_my_name(first_name, last_name=""):
    """Return sum
    Args:
        str(first_name,last_name)
    Raises:
        TypeError: if neither first_name or last_name is a string
        """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    first_name = str(first_name)
    last_name = str(last_name)

    print(f"My name is {first_name} {last_name}")
