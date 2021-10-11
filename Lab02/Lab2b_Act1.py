# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   2b-1
# Date:         8 9 2021
#

from math import *

#A)  Calculate the force in Newtons(N) applied to an object with a mass of 2 kg
#    and an acceleration of 5 m/s2. According to Newton’s Second Law the net
#    force applied to an object produces a proportional acceleration.

mass = 2 #kilograms
acceleration = 5 #m/s^2

force = mass * acceleration # Newtons
print("Force is", force, "N")

#B)  Calculate the wavelength of X-rays scattering from a crystal lattice
#    with a distance between crystal layers of 0.025 nm, scattering angle of
#    25 degrees, and first order diffraction. Bragg’s Law describes the
#    scattering of waves from a crystal using the equation

orderDiffraction = 1
distanceBetweenLayers = 0.025 # nanometers
scatteringAngle = 25 # degrees

wavelength = (2 * distanceBetweenLayers * sin(radians(scatteringAngle))) / orderDiffraction # nm
print("Wavelength is", wavelength, "nm")

#C)  The standard unit of wavelength in the SI system is nanometers (nm).
#    Calculate how much Radon-222 is left after 5 days of radioactive decay
#    given an initial amount of 3 g and a half-life of 3.8 days.

time = 5 # days
halfLife = 3.8 # days
initialAmount = 3 # grams

finalAmount = initialAmount * pow(2, -time / halfLife) # grams
print("Radon-222 left is", finalAmount, "g")

#D) Calculate the pressurein kPaof 5 moles of an ideal gas with a volume
#   of 0.15 m3, and temperature of 425 K. The Ideal Gas Law is the equation
#   of state of a hypothetical ideal gas and is a good approximation of
#   the behavior of gases under many conditions. Use a value of 8.314 m3Pa/K·mol
#   for the gas constant

amount = 5 # moles
volume = 0.15 # m^3
temperature = 425 # K
gasConstant = 8.314 # m^3 * Pa / (K * mol)

pressure = (amount * gasConstant * temperature) / volume # Pa
pressure /= 1000 # kPa
print("Pressure is", pressure, "kPa")