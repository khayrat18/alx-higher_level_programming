#!/usr/bin/python3
for num in range(10):
    for i in range(num + 1, 10):
        print("{0:d}{1:d}".format(num, i), end="")
        if num != 8 or i != 9:
            print(",", end="")
print()
