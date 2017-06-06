#!/usr/bin/python

# looking for a file named add
from add import add

# Main operations.

a = 2
b = 3
c = 6.0
d = 9.1
# My base program adding two numbers.
print "The result of adding is", a + b
# My base program calling my inline function.
print "The result of adding is", add(a,b)
print "The result of adding is", add(c,d)
