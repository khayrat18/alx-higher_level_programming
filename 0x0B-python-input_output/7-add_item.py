#!/usr/bin/python3
import sys

"""Adds all arguments to a  p   ython list and saves them to a file"""

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
if items is not None:
    items.extend(sys.argv[1:])
else:
    items = sys.argv[1:]

save_to_json_file(items, "add_item.json")