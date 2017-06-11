#!/usr/bin/python

#my adding function
def addInt(a, b):
  #declare a default return value.
  c = 0
  if isinstance(a,int) and isinstance(b,int):
    c = a + b

#return a value from our function
    return c
#main operations.

a = 2
b = 3
c = 5.0
d = 9.1

boo = "Casper the friendly ghost."

#my base program adding two numbers
print "The result of adding is", a + b

#my base program calling my inline function
print "The result of adding is", addInt(a,b)
