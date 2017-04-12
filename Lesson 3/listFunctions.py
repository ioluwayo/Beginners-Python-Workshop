# Created by ioluwayo on 2017-03-19.
# Python Lists come built-in with some very cool functions

# first lets consider the append() function
users = ["tom","matt", "chung", "mary"]
print users
users .append("willow")
print users # notice the difference?
# The append function adds an element to the end of a list.

# now lets consider the del() function
del users[0]# this deletes the element at index 0 from the list
print "List after deleting the first element:", users

#lets put the item back in the list
users.insert(0,"tom") # insert tom in at index 0 in the list
print users
# The insert() function puts an item at a specified index in a list and moves the other items right.
# [5,7,8].insert(2,4) will result in [5,7,4,8]

# now lets consider the pop() function
users.pop()
print users # notice the difference?
# the pop function deletes the last element in a list
# actually it deletes and returns it. Hmmm, that means we should have used a variable to store it
removedItem = users.pop()
print "The poped item is->",removedItem
print users
anotherRemovedItem = users.pop(0) # this pops out the item at index o
print users
# How do we access subsections of list . say index[5-10]
# we use a technique in python called slicing.
alphabets = ['a','b','c','d','e','f','g','h','i','j','k']
print alphabets
print alphabets[0:6] # print the section of the list starting from index 0 - index 5
print alphabets[0:8:2] # start:stop:step  remember this?
print alphabets[-1]
print alphabets[-2]
print alphabets[-11]
# so the negative sign means count from the back of the list. index -1 means the last element in the list
restAlphabets = ['l','m','o','p','q','r','s','t','u','v']
# lets join the lists together
alphabets.extend(restAlphabets)
print alphabets
# so the extend() function adds items from one list to the back of another.
# we could have done the same thing with a for loop.
lastLetters = ['w','x','y','z']
for i in lastLetters:
    alphabets.append(i)
print alphabets # our alphabet is complete.

# IS IT REALLY COMPLETE?
# lets check if the alphabet 'n' in there
print 'n' in alphabets # this prints False because i purposely left out 'n'
# the in operator allows you check if an item is in a list. it returns true of false.
result  = 'z' in alphabets
print result # True because 'z' is in the list
if 'n' in alphabets:
    print "List contains b"
else:
    print "List does not contain n"

# what if we want the index of an item in a list
print alphabets.index('c')
# be careful with the index() function it will throw an error is the item is not it the list.
try:
    alphabets.index('n') # remember n is not in the list
except ValueError as e:
    print e.message
    print "We handled the error gracefully"

# lets put 'n' in the list
alphabets.insert(13,'n') # counting from 0, n should be at location 13.
print alphabets




# python has some more cool functions
numbers = [1,3,7,70,50,100,-8,4,19]
print max(numbers) # returns the maximum element in the the list
print min(numbers)
print max(alphabets) # Hmm, well python returns the maximum in terms og alphabetical order
print min(['e','i','a','o','u']) # minimum element in alphabetical order

#lets consider reversing items in a list.
numbers.reverse() # this reverses the items in place. It does not return a new list. It stores the reversed list in
# the same variable.
print numbers
alphabets.reverse() # reverse the alphabets
print alphabets

# how about sorting the items in a list.
numbers.sort() # sorts the list in place. It does not return a new list
print "Sorted list",numbers
alphabets.sort() # should put it in alphabetical order
print alphabets

# Google lists in python to learn more about lists!.





