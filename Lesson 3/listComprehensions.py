# Created by ioluwayo on 2017-03-20.

# Python also supports computed lists,
# called list comprehensions
# In its simplest form, a list comprehension has the following syntax: L = [expression for variable in sequence]


# lets create a list containing the numbers 0 to 40
numbers = [1,2,3,4,5,6,7,8,9,10, "I am tired of typing :( "]
print numbers
# lets use list comprehension

numbers = [i for i in range(40)]
print numbers
# what did python do? remember that range is a sequence of numbers
# python appended the value of i to numbers as it went through the sequence.
# another example
ones = [1 for i in range(50)]
print ones
# or we could have done it this way.
twos = [] # create an empty list first
for i in range(50):
    twos.append(2) # append 2 to the list 50 times.
print twos

# lets create a list of all the even numbers in our previous list.
# This is our thought process.
# We loop though the entire list check if each item is divisible by 2 without remainder.
# if it is, we append it to a new list called evenNumbers

evenNumbers = []
for i in numbers:
    if i%2 == 0: # what does % mean?
        evenNumbers.append(i)
print evenNumbers

# is there a nicer way to do this?
# yes!
# lets use list comprehensions
evenNumbers = [i for i in numbers if i%2 == 0]
print evenNumbers
# lets try creating a list of odd numbers from our previous list
oddNumbers = [i for i in numbers if i%2 !=0]
print oddNumbers # isn't python amazing?!

