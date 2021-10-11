# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   3a-1-f
# Date:         13 9 2021
#

#takes in degrees in celcius and prints the equivalent degrees in Rankine
def celsiusToRankine(degreesCelsius):
    print("{:.2f} degrees Celsius is equivalent to {:.2f} degrees Rankine".format(degreesCelsius, degreesCelsius * (9/5) + 491.67))

celsiusToRankine(float(input("Please enter the number of degrees Celsius to be converted to degrees Rankine: ")))