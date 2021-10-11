# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   3b-1-a
# Date:         13 9 2021
#

#A)  Calculate the force in Newtons(N) applied to an object with a mass of 2 kg
#    and an acceleration of 5 m/s2. According to Newton’s Second Law the net
#    force applied to an object produces a proportional acceleration.

acceleration = 5 #m/s^2

print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): ")) # kg
acceleration = float(input("Please enter the acceleration (m/s^2): ")) # m/s^2

force = mass * acceleration # Newtons
print("Force is {:.1f} N".format(force))