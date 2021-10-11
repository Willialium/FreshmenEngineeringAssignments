# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   3a-1-e
# Date:         13 9 2021
#

#takes in liters per second (lps ) and prints the equivalent pounds per minute (galons per minute)
def lpsToGpm(liters):
    print("{:.2f} liters per second is equivalent to {:.2f} gallons per minute".format(liters, liters * 0.26417205 * 60))

lpsToGpm(float(input("Please enter the number of liters per second to be converted to gallons per minute: ")))