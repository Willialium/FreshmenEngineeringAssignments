# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   4b-1
# Date:         20 9 2021
#
#assign numbers
number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
number3 = float(input("Enter number 3: "))

#assume first is smallest
smallest = number1

#if the second or third are smaller than the first, set the smallest number equal to it
if(smallest > number2):
    smallest = number2
if(smallest > number3):
    smallest = number3

#print smallest
print("The smallest number is {}".format(smallest))