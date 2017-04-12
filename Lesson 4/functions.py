

# Step 1: Declare the function with the keyword def followed by the function name.

# Step 2: Write the arguments inside the opening and closing parentheses of the function,
# and end the declaration with a colon.

# Step 3: Add the program statements to be executed.

# Step 4: End the function with/without return statement.
# 1) function to print a message
def printme(msg):
    print msg


printme("First call")  # calling method


# 2) function that finds the avg of three numbers
def avg(num1, num2, num3):
    return sum([num1, num2, num3])/3

print avg(45, 32, 56)


# 3) function takes a list and sums all values more than a number
def sums(listofnums, num):
    result = sum(n for n in listofnums if n>=num)
    return result

# this is the actually program
l = map(int, raw_input("Enter numbers separated by space: ").split())
number = int(raw_input("What is your number: "))
print "The sum of all numbers more than ", number, " is ", sums(l, number)

# Great resources for Functions:
# https://www.codementor.io/python/tutorial/user-defined-functions-in-python-beginners

# We will go into more detail next class