#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    if my_list is None:
        my_list = []

    # looping through my list
    for list in reversed(my_list):
        print("{:d}".format(list))
