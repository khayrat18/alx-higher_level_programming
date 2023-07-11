#!/usr/bin/python3
"""A fuction that writes an objec to a text file"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON representation"""

    with open(filename, 'w') as fp:
        json.dump(my_obj, fp)
