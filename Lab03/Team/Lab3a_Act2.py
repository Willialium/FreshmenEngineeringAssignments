# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   3a-2
# Date:         13 9 2021
#

initialTime = float(input("Enter time 1: "))  # seconds
initialX = float(input("Enter the x position of the object at time 1: "))  # meters
initialY = float(input("Enter the y position of the object at time 1: "))  # meters
initialZ = float(input("Enter the z position of the object at time 1: "))  # meters
finalTime = float(input("Enter time 2: "))  # seconds
finalX = float(input("Enter the x position of the object at time 2: "))  # meters
finalY = float(input("Enter the y position of the object at time 2: "))  # meters
finalZ = float(input("Enter the z position of the object at time 2: "))  # meters

speedX = (finalX - initialX) / (finalTime - initialTime)  # m/s
speedY = (finalY - initialY) / (finalTime - initialTime)  # m/s
speedZ = (finalZ - initialZ) / (finalTime - initialTime)  # m/s

# creates an array of time interpolates
timeInterval = (finalTime - initialTime) / 4
timeList = []
x = initialTime
while x <= finalTime:
    timeList.append(x - initialTime)
    x += timeInterval


# takes in an index in the time interval array and returns a list with the values for that time interval
def interpolate(index):
    return [timeList[index] + initialTime,
            speedX * timeList[index] + initialX,
            speedY * timeList[index] + initialY,
            speedZ * timeList[index] + initialZ]

print()
print("At time {:.1f} seconds the object is at ({:.2f}, {:.2f}, {:.2f})".format(interpolate(0)[0], interpolate(0)[1],
                                                                                interpolate(0)[2], interpolate(0)[3]))
print("At time {:.1f} seconds the object is at ({:.2f}, {:.2f}, {:.2f})".format(interpolate(1)[0], interpolate(1)[1],
                                                                                interpolate(1)[2], interpolate(1)[3]))
print("At time {:.1f} seconds the object is at ({:.2f}, {:.2f}, {:.2f})".format(interpolate(2)[0], interpolate(2)[1],
                                                                                interpolate(2)[2], interpolate(2)[3]))
print("At time {:.1f} seconds the object is at ({:.2f}, {:.2f}, {:.2f})".format(interpolate(3)[0], interpolate(3)[1],
                                                                                interpolate(3)[2], interpolate(3)[3]))
print("At time {:.1f} seconds the object is at ({:.2f}, {:.2f}, {:.2f})".format(interpolate(4)[0], interpolate(4)[1],
                                                                                interpolate(4)[2], interpolate(4)[3]))
