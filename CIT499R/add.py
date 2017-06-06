#!/usr/bin/python
e = "Larry"
# My adding function.
def add(a, b):
  # Declare a default return value.
  c = 0
  # Check our parameters.
  if (isinstance(a,int) or isinstance(a,float)) and (isinstance(b,int) or isinstance(b,float)):
    c = a + b

    # print boo + " " + e

  # Return a value from our function.
  return c
