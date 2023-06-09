#!/usr/bin/python3
"""Creates an object from a JSON file"""

import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""

    with open(filename) as fp:
        return json.load(fp)
