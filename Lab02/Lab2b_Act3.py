# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   2b-3
# Date:         8 9 2021
#


#Use the fewst number of the following statements, in any combination,
# to output each of the following numbers

# x = 1
# x = y
# x += 1
# y = 10
# y += x
# y *= x
# z = 0
# z += x
# z += y

# 1
x = 1
z = 0
z += x
print(z)

# 25
z = 0
y = 10
x = 1
z += y
z += y
z += x
z += x
z += x
z += x
z += x
print(z)

# 102
z = 0
y = 10
x = y
y *= x
x = 1
z += y
z += x
z += x
print(z)

# 1000000000
z = 0
y = 10
x = y
y *= x
y *= x
x = y
y *= x
y *= x
z += y
print(z)

# 2468
z = 0
x = 1
y = 10
z += y
z += y
x += 1
y += x
y *= x
y *= x
z += y
x = y
y *= x
z += y
z += x
z += x
print(z)