# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   4b-3
# Date:         20 9 2021
#

day = int(input("Please enter a positive value for day: "))
widgets = 0

if day >= 0:
    # if between days 0 and 10
    if day <= 10:
        widgets += day * 10

    # if between day 10 and 50
    elif 10 < day < 50:
        widgets += 10 * 10
        widgets += (day) * (day + 1) / 2 - 55

    # if between 50 and 100
    elif 50 <= day <= 100:
        widgets += 10 * 10
        widgets += 1220
        widgets += 50 * (day - 50)

    # if greater than 100
    elif day > 100:
        widgets += 10 * 10
        widgets += 1220
        widgets += 50 * 50

    # print total
    print("The total number of widgets produced on day {:.0f} is {:.0f}".format(day, widgets))

# if negative
else:
    print("You entered an invalid number!")
