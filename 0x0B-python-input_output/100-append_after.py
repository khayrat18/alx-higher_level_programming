#!/usr/bin/python3
"""Inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line
    of text to a file, after each line
    containing a specific string"""

    text = ""
    with open(filename) as rf:
        for line in rf:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as wf:
        wf.write(text)
