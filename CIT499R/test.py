#!/usr/bin/python
# Define a local function.
def printMessage(whom):
  # Declare a global variable inside a function.
  global salutation
  # Assign a new value to an externally scoped variable.
  salutation = "Mrs."
  # Declare a local variable.
  message = "Hello " + salutation + " " + whom + "!"
  # Return a local variable.
  return message
# Define a program scope variable.
salutation = "Mr."
# Print the return value from the local function.
print printMessage("Marple")
