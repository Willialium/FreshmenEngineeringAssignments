# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   3b-2
# Date:         13 9 2021
#

from math import *

area = float(input("Please enter the area: "))

#Calculates radius of a circle given the area
def circleRadius(area):
    radius = sqrt(area/pi)
    return radius

#Calculates the side length of an equilateral triangle given the area
def triangleSide(area):
    side = sqrt(4 * area / tan(60*pi/180))
    return side

#Calculates the side length of a square given the area
def squareSide(area):
    side = sqrt(area)
    return side

#Calculates the side length of a pentagon given the area
def pentagonArea(area):
    side = sqrt(4 * area / (5 * tan(54 * pi / 180)))
    return side

#Calculates the side length of a dodecagon given the area
def dodecagonSide(area):
    side = sqrt(area / (3 * tan(75 * pi / 180)))
    return side

print("A circle with area {:.2f} has a radius {:.3f}".format(area, circleRadius(area)))
print("An equilateral triangle with area {:.2f} has a side {:.3f}".format(area, triangleSide(area)))
print("A square with area {:.2f} has a side {:.3f}".format(area, squareSide(area)))
print("A pentagon with area {:.2f} has a side {:.3f}".format(area, pentagonArea(area)))
print("A dodecagon with area {:.2f} has a side {:.3f}".format(area, dodecagonSide(area)))

