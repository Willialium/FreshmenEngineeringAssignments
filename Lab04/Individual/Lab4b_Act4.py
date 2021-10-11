# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   4b-4
# Date:         20 9 2021
#

from math import *

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))


def printRoots(A, B, C):
    if A == 0:
        if B == 0:
            print("You entered an invalid combination of coefficients")
        if B != 0:
            print("The root is x = {}".format(-1 * C / B))
        return

    # A != 0
    if B == 0:
        if C == 0:
            print("The root is x = 0")
        if C < 0:
            print("The roots are x = {} and x = {}".format(sqrt(-1 * C / A), -1 * sqrt(-1 * C / A)))
        if C > 0:
            print("The roots are x = {}i and x = {}i".format(sqrt(C / A), -1 * sqrt(C / A)))
        return

    # A != 0 and B != 0
    if (C == 0):
        print("The roots are x = 0.0 and x = {}".format(-1 * B / A))
        return

    # A != 0 and B != 0 and C != 0
    if B ** 2 - (4 * A * C) >= 0:
        root2 = (-B - sqrt((B ** 2 - 4 * A * C))) / (2 * A)
        root1 = (-B + sqrt((B ** 2 - 4 * A * C))) / (2 * A)
        if root1 == root2:
            print("The root is x = {}".format(root1))
        else:
            print("The roots are x = {} and x = {}".format(root1, root2))
    else:
        root2 = str(-B / (2 * A)) + " - " + str((sqrt(-1 * (B ** 2 - 4 * A * C)) / (2 * A))) + "i"
        root1 = str(-B / (2 * A)) + " + " + str((sqrt(-1 * (B ** 2 - 4 * A * C)) / (2 * A))) + "i"
        print("The roots are x = {} and x = {}".format(root1, root2))


printRoots(A, B, C)
