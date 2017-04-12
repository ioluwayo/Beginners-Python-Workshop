# Created by ioluwayo on 2017-03-19.

#To create a list, put a number of items in square brackets.

myList = [1,"word",7, 5]
# this means that   1 is located at position 0 in in the list.
#                   "word" is located at position 1 in the list.
#                   7 is located at position 2 in the list.
#                   5 is located at position 3 in the list.
# Notice that the list has 4 items but the last item is at location 3. In programming we start counting from 0.
print myList[0]
print myList[1]
print myList[2]
print myList[3]
# 0, 1, 2, 3 are called indexes. They are used to specify the location of an item in a lists.

#python allows you print an entire list
print myList

# creating an empty list
anEmptyList = []
# print the lenght of you list. ie the number of items in the list
print "Length of myList is: ",len(myList)
print "Length of the empty list is: ",len(anEmptyList)
print
print "---------------------------------------------------------"


#You can change the value of item in a list by using the index.
myList[1] = 3
print myList
# see the difference?


print
print "---------------------------------------------------------"

courses = ["CHE 100","BME 200", "MTH 103", "BLG 100"]
#You can loop through all items in a list using  a for loop.
for i in range(len(courses)):
    print courses[i]

# what is happening here?

#The first time the loop runs, i will be 0. # so we are essential doing print courses[0]
#The next time the loop runs, i will be 1, so we are doing print courses[1]
#This continues until we get to 3. Remember how the range function works in python. range(4) is 0, 1, 2, 3.

#There is an easier way to loop through all items in a list in python.
for x in myList:
    print x, # notice the effect of the comma?
# what is happening here?
#python goes through every item in the list one after the other. x refers to the current item python is at.
# so by printing x we are printing the current item as python goes through all the items.

# another interesting way of getting all the elements in a list.
print
print "---------------------------------------------------------"
for index, item in enumerate(courses):
    print index, item
    #The enumerate function goes through the list and returns index, courses[index].
    # so we print the 2 items returned every time is reaches a new location in the list
# we will look at more interesting things about list soon.