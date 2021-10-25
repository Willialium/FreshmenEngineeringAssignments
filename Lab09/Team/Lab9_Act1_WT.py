# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   Lab 9-1-WT
# Date:         25-10-2021
#

tempList = []#list of temperatures
volumeList5 = []#list of volumes at 5 kPa
energyList5 = []#list of volumes at 5 kPa
enthalpyList5 = []#list of volumes at 5 kPa
entropyList5 = []#list of volumes at 5 kPa
volumeList10 = []#list of volumes at 10 kPa
energyList10 = []#list of internal energys at 10 kPa
enthalpyList10 = []#list of enthalpys at 10 kPa
entropyList10 = []#list of entropys at 10 kPa
userVal = 0#users inputed temperature
outputs = []#a list of the four calculated values
pressure = 0#The pressure we are doing math with


#################################
####### PROCESS USER DATA #######
###### WILLIAM AND HENRY ########

# Locate the range the user data falls between
# Go through each value in the list until the input is greater than a value, then that value and the next are the bounds


for i in tempList:
    if i > userVal:
        minIndex = tempList.index(i)
        break

maxIndex = minIndex + 1

# Get an intropolation function for each range
# Find the change in temperature between user data and the lowest range
# Find slope between the range values

# Calculate values based off of the intropolation function
# Return a list containing each calculated value