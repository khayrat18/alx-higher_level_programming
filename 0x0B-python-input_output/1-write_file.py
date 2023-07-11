#!/usr/bin/python3
"""Writes a string to a text file and return number of charactes"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file
    and returns number of characters writtwn
    """

    with open(filename, 'w', encoding='utf-8') as fp:
        return fp.write(text)
