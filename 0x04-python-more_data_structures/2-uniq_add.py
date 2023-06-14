#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is None:
        my_list = []
    seen = set()
    count = 0
    for num in my_list:
        if num not in seen:
            seen.add(num)
            count += num
    return count
