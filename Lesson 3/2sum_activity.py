# Created by ioluwayo on 2017-03-20.
"""
This program is called 2 sum. It is a popular programming challenge giving at tech interviews.
You are given two inputs. A list containing numbers e.g numbers = [1,3,4,8,7] and a number e.g sum = 5
You are to check if any 2 numbers in the list of numbers add up to the given number.
You need to find if there is a pair of numbers in the list that add up to the sum given.

So in the first example.
You program will say YES. This is because 1 + 4 gives us 5
if numbers = [1,3,6,8,7]
Your program will say NO . This is because no numbers sum up to give 5

"""

def twoSum(numbers, s):
    for i in range(len(numbers)): # loop through all the items
        for j in range(i+1,len(numbers)): # loop through the rest of the items. Starting from the next. i+1
            if numbers[i] + numbers[j] == s: # check if they add up to the summ
                return "YES"
    return "NO" # if the program gets here, that means it never got into the if statement, so no pair exists.

# there is a more efficient way of solving this problem. We will re-visit it after we look at dictionaries.