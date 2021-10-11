# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab 4-1
# Date:         24 9 2021
#

from math import *

print("Enter the hours parked as a decimal number. Include a negative sign if the ticket is lost.")
hours = float(input("Please enter the hours parked: "))


# Takes in the number of hours and returns the price
def fee(numHours):
    fee = 0

    # If negative
    if (numHours < 0):
        fee += 36
        numHours *= -1
    numHours = ceil(numHours)
    # Adds fees per day and sets numHours equal to the amount of hours on the last day
    days = numHours // 24
    fee += 24 * days
    numHours = numHours % 24

    # If less than 2 hours
    if 0 < numHours <= 2:
        fee += 4

    # If between 2 and 4 hours
    elif 2 < numHours <= 4:
        fee += 7

    # If between 4 and 21 hours
    elif 4 < numHours < 21:
        fee += 7
        fee += (numHours - 4)

    # If greater than 21 hours (But still less than 24 because we are in the last day)
    elif numHours >= 21:
        fee += 24

    return fee


# Prints the fee
print("Parking for {} hours please pay ${}".format(hours, fee(hours)))
