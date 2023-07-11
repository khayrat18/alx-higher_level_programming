#!/usr/bin/python3
"""Defines a fuction that reads an file and print to stdout"""


def read_file(filename=""):
    """Function that reads a text file and prints to stdout"""

    with open(filename, encoding="utf-8") as fp:
        print(fp.read(), end="")
