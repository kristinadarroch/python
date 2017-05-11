#!/usr/bin/python
# Declare variables.
a = 2
b = 5
c = 8
guess = raw_input("Enter a number: ")
try:
  guess = int(guess)
except ValueError:
  try:
    guess = float(guess)
  except ValueError:
    print "You entered a string, please enter a number."
finally:
  if 2 <= guess <= 8:
    print "Just right ..."
  elif not isinstance(guess,basestring):
    if guess < 2:
      print "Too low ..."
    elif guess > 8:
      print "Too high ..."
