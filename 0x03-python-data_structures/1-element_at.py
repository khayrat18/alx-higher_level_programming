#!/usr/bin/python3

def element_at(my_list, idx):

    for idx in my_list:
        if (idx < 0) and (idx > my_list):
            return None
    return(idx - 1)
