# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   7b-2a
# Date:         12-10-2021
#

# Initialized variables

prices = ""
values = []

# Creates a list of the values
# If there is no decimal, it adds .00 to the end
# If finds the longest number to calculate the offset later
def getValues():
    maxi = 0
    prices = input("Enter three or more prices separated by spaces: ")
    for price in prices.split(" "):
        if "." not in price: # Adds a .00 to every number without a decimal
            price += ".00"
        values.append(price)
        maxi = max(maxi, len(price)) # maxi is set to the longest number
    return maxi # length of longest number


maxLength = getValues() # Length of longest number used in creating offsets

# Prints each value but off sets it based on the largest number
# so that the largest number is only one space away from the dollar sign '$'
if len(values) < 3:
    print("Please enter three or more values")
    maxLength = 0
    getValues()
for price in values:
    print("$ ", end="")
    for i in range(0, maxLength - len(price)):
        print(" ", end="")
    print(price)
