# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   3a-1-b
# Date:         13 9 2021
#

#takes in kilometers and prints the equivalent miles
def kiloToMile(kilo):
    miles = kilo * .6214
    miles = int(miles * pow(10,2))
    miles /= pow(10,2)
    print("{:.2f} kilometers is equivalent to {} miles".format(kilo, miles))

kiloToMile(float(input("Please enter the number of kilometers to be converted to miles: ")))