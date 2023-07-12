#!/usr/bin/python3
"""Dictionary description of a simple data structure"""


def class_to_json(obj):
    """Returns the dictionary description of a simple
    data structure"""

    return obj.__dict__
