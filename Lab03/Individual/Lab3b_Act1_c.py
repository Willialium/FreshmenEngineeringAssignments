# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   3b-1-c
# Date:         13 9 2021
#

#C)  The standard unit of wavelength in the SI system is nanometers (nm).
#    Calculate how much Radon-222 is left after 5 days of radioactive decay
#    given an initial amount of 3 g and a half-life of 3.8 days.

halfLife = 3.8 # days

print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days): ")) # days
initialAmount = float(input("Please enter the initial amount (g): ")) # grams

finalAmount = initialAmount * pow(2, -time / halfLife) # grams
print("Radon-222 left is {:0.2f} g".format(finalAmount))