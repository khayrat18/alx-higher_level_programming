#!/usr/bin/python3

# import module
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

# declare variables
a = 10
b = 5

# printing result of the function

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
