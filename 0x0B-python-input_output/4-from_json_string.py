#!/usr/bin/python3
"""Returns object representated by a JSON string"""

import json


def from_json_string(my_str):
    """Returns an object representated by a JSON string"""

    return json.loads(my_str)
