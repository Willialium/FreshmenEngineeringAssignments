# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab 6a-1a
# Date:         4 10 2021
#

sideLength = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
gold = 0

for i in range(1, layers+1):
    gold += (i + i-1)
    gold += 4*i

print("You need {:.2f} square meters of gold foil to cover the pyramid".format(gold * sideLength**2))

