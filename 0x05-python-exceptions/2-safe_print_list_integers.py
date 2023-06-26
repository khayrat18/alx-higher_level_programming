#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for idx in my_list[:x]:
            if isinstance(idx, int):
                print("{:d}".format(idx), end="")
                count += 1
        print()
    except TypeError:
        pass
    finally:
        return (count)
