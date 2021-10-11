# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   2a-3
# Date:         10 9 2021
#

from math import *

#Part 1
print("Part 1:")

initialLocation = 2025 # kilometers
finalLocation = 23025 # kilometers
initialTime = 10 # minutes
finalTime = 55 # minutes

slope = (finalLocation - initialLocation) / (finalTime - initialTime) #kilometers / minute

givenTime = 25 # minutes
desiredDistance = slope * (givenTime - initialTime) + initialLocation # kilometers

if(givenTime > initialTime or givenTime < finalTime):
    print("For t =", givenTime, "minutes, the position p =", desiredDistance, "kilometers")
else:
    print("The time is not in the bounds for interpolation")


print("Part 2:")

radius = 6745 # kilometers
initialTime = 10 # minutes
finalTime = 55 # minutes
initialLocation = 2025 # kilometers
finalLocation = 23025 # kilometers

circumference = 2 * pi * radius # kilometers

givenTime = 5 # hours
givenTime *= 60 # minutes

slope = (finalLocation - initialLocation) / (finalTime - initialTime) #kilometers / minute
desiredDistance = slope * (givenTime - initialTime) + initialLocation # kilometers

desiredDistance %= (circumference / 2) # kilometers

if(givenTime > initialTime or givenTime < finalTime):
    print("For t =", givenTime / 60, "hours, the position p =", desiredDistance, "kilometers")
else:
    print("The time is not in the bounds for interpolation")

