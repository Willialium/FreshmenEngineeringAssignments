# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   4b-2
# Date:         20 9 2021
#

########### Part A ##########

a = 1 / 7
print("a =", a)
b = a * 7
print("b = a * 7 =", b) # b equals and prints 1.0

c = 2 * a
d = 5 * a
f = c + d
print("f = 2 * a + 5 * a =", f) # prints 0.9999999999999

from math import sqrt
x = sqrt(1/3)
print("x =", x)
y = x * x * 3
print("y = x * x * 3 =", y) # prints 1.0
z = x * 3 * x
print("z = x * 3 * x =", z) # prints 0.9999999999999

########### Part B ##########

TOL = 1e-10
# check if b and f are equal within specified tolerances
if abs(b - f) < TOL:
    print("b and f are equal within tolerance of", TOL)
else:
    print("b and f are NOT equal within tolerance of", TOL)

TOL = 1e-10
# check if b and z are equal within specified tolerances
if abs(b - y) < TOL:
    print("y and z are equal within tolerance of", TOL)
else:
    print("y and z are NOT equal within tolerance of", TOL)


########### Part C ##########

m = 0.1
print("m =", m)
n = 3 * m
print("n = 3 * m = 0.3", n == 0.3)
p = 7 * m
print("p = 7 * m = 0.7", p == 0.7)
q = n + p
print("q = 1", q == 1)
