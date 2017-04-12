# Original Code:
# ----------------
#
#  name1 = "SDZ"
# address1 = "159 Dalhouse Street"
#
# name2 = "Ryerson"
# address2 = "350 Victoria Street"
#
# name_entered = raw_input("Enter name: ")
#
# if name_entered == name1:
#     print(address1)
# elif name_entered == name2:
#     print(address2)
# else:
#     print("Address not found")
#

# Re-fractored Code with use of Dictionary:
# -----------------------------------------

addresses = {
            "SDZ": "159 Dalhouse Street",
            "RYERSON": "350 Victoria Street"
}

name_entered = raw_input("Enter name: ")
print addresses.get(name_entered.upper(), "Address not found")

# Or you can write that as one line so essentially your program becomes
# only two lines. One to define database and one to get whatever
# address the user needs:

print addresses.get(raw_input("Enter name: ").upper(), "Address not found")
