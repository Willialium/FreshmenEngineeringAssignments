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
userVal = 0#users inputted temperature
userPressure = 0#users inputted pressure
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


##########################
##### EXTRA CREDIT #######

def newInterpolate(actualPressure):

    # Get the four values at kPa = 5 and 10
    values1 = interpolate(userVal, minIndex, maxIndex, 5)
    values2 = interpolate(userVal, minIndex, maxIndex, 10)

    # For each value, interpolate the four values using pressure as the x axis
    # and the values as the y axis between kPa = 5 and 10
    newVolumeSlope = (values1[0] - values2[0]) / 5
    newVolume = newVolumeSlope * (actualPressure - 5) + values1[0]

    newEnergySlope = (values1[1] - values2[1]) / 5
    newEnergy = newEnergySlope * (actualPressure - 5) + values1[1]

    newEnthalpySlope = (values1[2] - values2[2]) / 5
    newEnthalpy = newEnthalpySlope * (actualPressure - 5) + values1[2]

    newEntropySlope = (values1[3] - values2[3]) / 5
    newEntropy = newEntropySlope * (actualPressure - 5) + values1[3]

    # Return the four in the order they will be printed
    return [newVolume, newEnergy, newEnthalpy, newEntropy]


