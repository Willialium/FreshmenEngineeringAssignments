# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   3a-1-a
# Date:         13 9 2021
#

#takes in pounds and prints the equivalent newtons
def poundsToNewtons(pounds):
    print("{:.2f} pounds is equivalent to {:.2f} Newtons".format(pounds, pounds*4.44822))

poundsToNewtons(float(input("Please enter the number of pounds to be converted to Newtons: ")))
