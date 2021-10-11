# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   2b-2a
# Date:         8 9 2021
#

initialX = 2 #meters
initialY = 3 #meters
initialZ = 7 #meters
initialTime = 12 #seconds

finalX = 25 #meters
finalY = -5 #meters
finalZ = 11 #meters
finalTime = 85 #seconds

time = 45 #seconds

xSpeed = (finalX - initialX) / (finalTime - initialTime) # m/s
ySpeed = (finalY - initialY) / (finalTime - initialTime) # m/s
zSpeed = (finalZ - initialZ) / (finalTime - initialTime) # m/s

xDisplacement = xSpeed * (time - initialTime) #meters
yDisplacement = ySpeed * (time - initialTime) #meters
zDisplacement = zSpeed * (time - initialTime) #meters

print("At time", time, "seconds:")
print("x0 =", xDisplacement + initialX, "m")
print("y0 =", yDisplacement + initialY, "m")
print("z0 =", zDisplacement + initialZ, "m")
