import math
try:
    userOption =  int(raw_input("Enter 1, 2, or 3: "))
except ValueError:
    print "Wrong value"
    exit()

while userOption !=3:
    if userOption == 1:
        length = float(raw_input("Enter the length of the square: "))
        print length*length, "is your Area"
    elif userOption == 2:
        radius = float(raw_input("Enter the radius of the circle: "))
        print math.pi*radius*radius, "is your Area"
    else:
        print "Wrong input. Try again"
    userOption = int(raw_input("Enter 1, 2, 3:"))
print "Program ended"