# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   7b-1
# Date:         12-10-2021
#

name = input("What is your name? ")  # Gets the name from the user
vowelList = ["A", "E", "I", "O", "U", "Y"]  # List of vowels to check if the name starts with a vowel
rhymeName = ""  # The name that will be used in the rhymes

if(name[:1] in vowelList):  # Creates the rhyme name depending on if it starts with a vowel or not
    rhymeName = chr(ord(name[:1])+32) + name[1:]
else:
    rhymeName = name[1:]


#  Prints the rhyme

print("{}, {}, Bo-B{}".format(name, name, rhymeName))
print("Banana-Fana Fo-F{}".format(rhymeName))
print("Me Mi Mo-M{}".format(rhymeName))
print("{}!".format(name))