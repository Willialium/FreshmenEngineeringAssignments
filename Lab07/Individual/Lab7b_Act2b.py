# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   7b-2b
# Date:         12-10-2021
#

values = input("Enter three or more values separated by spaces: ").split(" ")  # Gets a list of the values from the user
splitter = input("Enter a two-character separator: ")  # Gets a separator

print(values[0], end="")  # Prints the first number
for value in values[1:]:  # Prints the separator followed by the next number for each remaining value
    print(" {} ".format(splitter), end=value)
