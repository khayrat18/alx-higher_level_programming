#!/usr/bin/python3

#import a  module
import calculator_1 

#declare variables
a = int(10)
b = int(5)

#printing result of the function

print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))

