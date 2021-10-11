# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   3b-1-d
# Date:         13 9 2021
#

#D) Calculate the pressurein kPaof 5 moles of an ideal gas with a volume
#   of 0.15 m3, and temperature of 425 K. The Ideal Gas Law is the equation
#   of state of a hypothetical ideal gas and is a good approximation of
#   the behavior of gases under many conditions. Use a value of 8.314 m3Pa/K·mol
#   for the gas constant

gasConstant = 8.314 # m^3 * Pa / (K * mol)

print("This program calculates the pressure given moles, volume, and temperature")
amount = float(input("Please enter the number of moles: ")) # moles
volume = float(input("Please enter the volume (m^3): ")) # m^3
temperature = float(input("Please enter the temperature (K): ")) # K

pressure = (amount * gasConstant * temperature) / volume # Pa
pressure /= 1000 # kPa
print("Pressure is {:.0f} kPa".format(pressure))