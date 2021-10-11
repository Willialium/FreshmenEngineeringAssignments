# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   3a-1-c
# Date:         13 9 2021
#

#takes in atmospheres and prints the equivalent milimeters of murcury (mm Hg)
def atmosphereToMmHG(atmosphere):
    print("{:.2f} atmospheres is equivalent to {:.2f} millimeters of mercury".format(atmosphere, atmosphere * 760))

atmosphereToMmHG(float(input("Please enter the number of atmospheres to be converted to millimeters of mercury: ")))