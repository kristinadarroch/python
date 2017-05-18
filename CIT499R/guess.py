#!/usr/sbin/Python

# What we should learn:
# 1. How to import a module or library.
# 2. How to create variables and assign them values.
# 3. How to print messages.
# 4. How to write a loop.
# 5. How to write an if-else statement, and a colon follows the if and the else
# 6. How to write an if-elif statement, and a colon follows the if and elif lines.
# 7. Indentation is not consmetic, and only follows a colon!
# 8. The = symbol assigns a value
# 9. The <, >, <=, >=, == compare values
# 10. There is no unary operator in Python, we increment by assigning a variable
# itself + 1
# 11. != is not equal

#-------------------------------------------------------------------
# In Linux or Unix, the first line should use a # and then an ! to indicate a subshell
# and should be followed by the fully qualified path to the Python executable
#-------------------------------------------------------------------
# Change the execution privliages of the file
# $ chmod 755 guess.py
#-------------------------------------------------------------------

import random, easygui
secret = random.randint(1, 99)
guess = 0
tries = 0
easygui.msgbox("""  Ahoy! I'm the Dread Pirate Robers, and I have a secret!It is a number from 1 to 99. I'll give you six tries""")

while guess != secret and tries < 6:
    guess = easygui.integerbox(" What's yer guess, matey?")
    if not guess: break
    if guess < (secret - 20):
        easygui.msgbox(str(guess) + " is way too low ye scurvy dog!")
    if guess >= (secret - 20) and guess <= (secret - 10):
        easygui.msgbox(str(guess) + " it is too low doggie")
    if (secret - 10) < guess < (secret - 5):
        easygui.msgbox(str(guess) + " hmmmmmmmm...something...but it's low...")
    if guess >= (secret - 5) and guess < secret:
        easygui.msgbox(str(guess) + " is close, but no. It be too low matey...")
    if guess <= (secret + 5) and guess > secret:
        easygui.msgbox(str(guess) + " is close, but too high, matey!")
    if (secret + 5) < guess < (secret + 10):
        easygui.msgbox(str(guess) + " hmmmmm...something...but it's high...")
    if guess <= (secret + 20) and guess >= (secret + 10):
        easygui.msgbox(str(guess) + " Arr! Too high, ye be!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " it is too high, landlubber!")
    tries = tries + 1

if guess == secret:
    easygui.msgbox(str(guess) + " Avas! Ye got it! Found my secret, ye did!")
else:
    easygui.msgbox("  No more guesses! The number was " + str(secret))


#AFTER EVERY SINGLE COLON THERE NEEDS TO BE AN INDENT
