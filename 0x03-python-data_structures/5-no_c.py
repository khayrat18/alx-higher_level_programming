#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for rem in my_string:
        if rem != 'c' and rem != 'C':
            new_string += rem
    return new_string