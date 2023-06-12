#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = 0
    if my_list is None:
        my_list = []
    for num in my_list:
        if num > largest:
             largest = num
    return largest
