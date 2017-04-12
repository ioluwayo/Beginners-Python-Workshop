#usr/bin/python
# Created by ioluwayo on 2017-03-07.

import random
# this is how to use python's random number generator method.
# You can read up on how it works on the python website.
# for the purpose of the lesson today it suffices to know that a random integer between x(inclusive) and y(inclusive)
# is returned by the method every time it runs.
number = random.randint(1,2)

# we need to use the int() method to convert our string to an integer. we could use the float function too.
guess = int(raw_input("Guess the number: "))

# The while loop will continue to repeat as long as the condition is true.
while guess != number:
    if guess > number:
        print "Your guess is too high"
    else:
        print "Your guess is too low"
    guess = int(raw_input("Guess the number: "))

# python only gets here if the condition for the while loop is false
print "\nYou guessed right!!"
print "The random number generated was: ",number
print "Your guess is: ", guess