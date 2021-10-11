# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab 6a-1b
# Date:         4 10 2021
#
#Enter the side length in meters:
# Enter the number of layers:
# You need 5.00 square meters of gold foil to cover the pyramid
sideLength = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))
gold = 0

gold += layers**2
gold += 4 * (1/2 * layers*(layers+1))

print("You need {:.2f} square meters of gold foil to cover the pyramid".format(gold * sideLength**2))