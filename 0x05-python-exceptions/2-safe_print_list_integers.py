#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    prnt = 0
    for idx in my_list:
        try:
            if count < x:
                print("{:d}".format(idx), end="")
                count += 1
                prnt += 1
            else:
                break
        except (TypeError, ValueError):
            count += 1
            continue
    print()
    return (prnt)
