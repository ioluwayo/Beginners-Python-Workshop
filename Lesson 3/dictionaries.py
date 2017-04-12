# Dictionaries

# how to define custom dictionary
ages = {'John': 21, 'Mary': 25, 'Bob': 43}
print ages['Mary']
name = raw_input("Enter name: ") # Let's try to lookup a value
current_age = ages.get(name)
print current_age

# What if the key doesn't exist?
print ages.get('H') #We get none

# We can also set our own default message or value
print ages.get('H', "Doesn't Exist")

# To remove a key-value pair we 'pop'
# it out of the structure. This returns the popped item.
# You can chose to store it or not
print "\n", ages
print ages.pop('John')
print ages

# If we pop a key that doesn't exist there's an error
# We get avoid this similar to the .get() function
print ages.pop('John', 'Nothing Found')


# ----------------------
# More tricks:
# You can run each section individually to understand the code
# Simply highlight code, right click and select "Execute Line in Console"

# How to add new value
ages = {'John': 21, 'Mary': 25, 'Bob': 43}
print ages
newName = raw_input("Enter name to add: ")
newAge = int(raw_input("Enter age: "))
ages[newName] = newAge
print ages

# exploiting pop to return anything we want
ages = {'John': 21, 'Mary': 25, 'Bob': 43}
var = ages.pop('dd', {1: 'ee', 3: "rr"}) # We are returning a new Dictionary if the value isnt there!

# Can you interpret this code?
if isinstance(var, dict):
    print 'Dictionary Returned'
elif isinstance(var, int):
    print 'Integer Returned'


# How to Loop through all values in a dictionary

# This only print the keys
for k in {'John': 21, 'Mary': 25, 'Bob': 43}:
    print k

# This makes all keys and their value available
# for you to use however you wish
ages = {'John': 21, 'Mary': 25, 'Bob': 43}
print ages
for k, v in ages.items():  # notice the .items() !
    print k, v+200
print len(ages)

# Filling a dictionary with values from a file!
# In this example it is assumes that the file has only two values per line
# if more exist you would have to decide what is the key and what is the value
# after the line.split() .
# Note the file you are trying to access must be in the same location as
# the .py that is trying to access it otherwise the full path
# to that file must be specified
d = {}
with open("file.txt") as f:
    for line in f:
       (key, val) = line.split()
       d[int(key)] = val