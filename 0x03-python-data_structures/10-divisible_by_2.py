#!/usr/bin/python3
   
def divisible_by_2(my_list=[]):
    result = []
    if my_list is None:
        my_list = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result