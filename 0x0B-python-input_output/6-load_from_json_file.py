#!/usr/bin/python3

import json

"""Creates an object from a JSON file"""


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""

    with open(filename) as fp:
        json.load(fp)
