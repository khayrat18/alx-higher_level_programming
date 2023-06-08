#!/usr/bin/python3

if __name__ == "__main__":
 import sys

if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("1 argument:")
    print("{}: {}".format(1, sys.argv[1]))
else:
    print("{} arguments:".format(len(sys.argv)-1))
    # looping through the arguments
    for x in range(1, len(sys.argv)):
        print("{}: {}".format(x, sys.argv[x]))
