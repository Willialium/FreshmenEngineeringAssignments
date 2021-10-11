# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   3b-challenge
# Date:         13 9 2021
#

from math import *

digits = int(input("Please enter the number of digits of precision for pi: "))
str = "The value of pi to {} digits is: {:." + str(digits) + "f}"
print(str.format(digits, pi))