# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   3b-1-b
# Date:         13 9 2021
#

from math import *

#B)  Calculate the wavelength of X-rays scattering from a crystal lattice
#    with a distance between crystal layers of 0.025 nm, scattering angle of
#    25 degrees, and first order diffraction. Bragg’s Law describes the
#    scattering of waves from a crystal using the equation

print("This program calculates the wavelength given distance and angle")
distanceBetweenLayers = float(input("Please enter the distance (nm): "))
scatteringAngle = float(input("Please enter the angle (degrees): "))

orderDiffraction = 1

wavelength = (2 * distanceBetweenLayers * sin(radians(scatteringAngle))) / orderDiffraction # nm
print("Wavelength is {:0.4f} nm".format(wavelength))