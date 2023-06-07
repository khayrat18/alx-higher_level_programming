#!/usr/bin/python3

for x in range(ord('z'), ord('A')-1, -1):
    if x % 2 == 0:
        print("{}".format(chr(x)), end="")
    else:
        print("{}".format(chr(x).upper()), end="")


