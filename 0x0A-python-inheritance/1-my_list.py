# #!/usr/bin/python3
"""Defines a class"""
class MyList(list):
    """ A class MyList inherests of list"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print (sorted_list)
