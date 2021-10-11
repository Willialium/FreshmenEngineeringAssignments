# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   1b-2
# Date:         6/9/2021
#

from math import *



#Question A: Calculate Force (N) applied to an object of 2 kg and an acceleration of 5 m/s^2

force_N = 0
mass_kg = 2
acceleration_ms2 = 5

force_N = mass_kg * acceleration_ms2 #from the equation

print("Force is", 10, "N")



#Question B: Calculate the wavelength of X-rays scattered from a crystal lattice with a distance between layers
#of 0.025 nm, scattering angle of 25 degrees, and first order diffraction

order_of_diffraction = 1
wavelength_nm = 0
distanceBetweenLayers_nm = 0.025
scatteringAngle_degrees = 25

wavelength_nm = (2 * distanceBetweenLayers_nm * sin(radians(scatteringAngle_degrees))) / order_of_diffraction #from the equation

print("Wavelength is", wavelength_nm, "nm")



#Question C: How much Radon-222 is left after 5 days of radioactive decay given an initial amount of
#3g and a half-life of 3.8 days

finalRadon_g = 0
initialRadon_g = 3
halfLife_days = 3.8
timePassed_days = 5

finalRadon_g = initialRadon_g * pow(2, (-timePassed_days / halfLife_days)) #from the equation

print("Radon-222 left is", finalRadon_g, "g")



#Question 4: Calculate the pressure in kPa of an ideal gas with a volume of 0.15 m^3, and a temperature of 435 k
#Use 8.314 m^3 * Pa/k*mol for the gas constant

gas_moles = 5
gasVolume_m3 = 0.15
temperature_K = 425
gasConstant_value = 8.314

pressure_kPa = ((gas_moles * gasConstant_value * temperature_K) / gasVolume_m3) #Formula for pressure in Pa
pressure_kPa /= 1000 # converting to kPa
print("Pressure is", pressure_kPa, "kPa")