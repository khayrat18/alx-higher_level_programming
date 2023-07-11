#!/usr/bin/python3


def append_write(filename="", text=""):
    """Function that appends a string
    to the end of a text file
    """

    with open(filename,'a', encoding='utf-8') as fp:
        count = fp.write(text)
    return count
