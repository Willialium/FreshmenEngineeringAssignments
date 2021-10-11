# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   3a-1-d
# Date:         13 9 2021
#

#takes in watts and prints the equivalent BTU per hour (BTU ph)
def wattsToBTUph(watts):
    BTU = watts * 3.412142
    print("{:.2f} watts is equivalent to {:.2f} BTU per hour".format(watts, BTU))

wattsToBTUph(float(input("Please enter the number of watts to be converted to BTU per hour: ")))