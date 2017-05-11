#!/usr/bin/python
again = 'y'
print "This program can create a multiplication table for you."
while again == 'y':
    print "Which table would you like?"
    number = raw_input()
    try:
        number = int(number)
        if number >= 12:
            for i in range(number + 1):
                print i, "X", number, "=", number*i
        elif number < 12:
            for i in range(13):
                print i, "X", number,"=", number*i
    except ValueError:
        print "That was not an integer. Please enter an integer (a whole number)."
    print "Try again? Enter 'y' for yes and 'n' for no."
    try:
        again == 'y' or again == 'n'
        again == 'y'
    except ValueError:
        print "Please enter 'y' for yes and 'n' for no."
        again = raw_input().lower()
print "Thank you. I hope this was useful. Have a nice day."
