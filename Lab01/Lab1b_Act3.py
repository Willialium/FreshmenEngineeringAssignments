# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   1b-3
# Date:         6/9/2021
#

from math import exp

# f(x) = (e^x - 1)/x evaluated close to x = 0. Use values of x ranging
# from 1 to 10^-7 in steps of 1/10 of the previous value

print("This shows the evaluation of (e^x-1)/x evaluated close to x=0")
print("My guess is 1.0")

x = 1                   #x = 1
print((exp(x) - 1)/x)

x = 0.1                 #x = 1 * 10^-1
print((exp(x) - 1)/x)

x = 0.01                #x = 1 * 10^-2
print((exp(x) - 1)/x)

x = 0.001               #x = 1 * 10^-3
print((exp(x) - 1)/x)

x = 0.0001              #x = 1 * 10^-4
print((exp(x) - 1)/x)

x = 0.00001             #x = 1 * 10^-5
print((exp(x) - 1)/x)

x = 0.000001            #x = 1 * 10^-6
print((exp(x) - 1)/x)

x = 0.0000001           #x = 1 * 10^-7
print((exp(x) - 1)/x)

print("\nMy guess was close and would be accurate if x got infinitely close to 0")
