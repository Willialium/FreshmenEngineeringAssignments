
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab 9-1
# Date:         25-10-2021
#

#################################
###### GET ALL DATA NEEDED ######
############ DAVID ##############

# Hardcode all of the data in the excel file in a list
tempList = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260] #list of temperatures
volumeList5 = [0.0009977, 0.0009996, 0.0010057, 0.0010149, 0.0010267, 0.0010410, 0.0010576, 0.0010769, 0.0010988, 0.0011240, 0.0011531, 0.0011868, 0.0012268, 0.0012755] #list of volumes at 5 kPa
energyList5 = [0.04, 83.61, 166.92, 250.29, 333.82, 417.65, 501.91, 586.8, 672.55, 759.47, 847.92, 938.39, 1031.6, 1128.5] #list of internal energies at 5 kPa
enthalpyList5 = [5.03, 88.61, 171.95, 255.36, 338.96, 422.85, 507.19, 592.18, 678.04, 765.09, 853.68, 944.32, 1037.7, 1134.9] #list of enthalpys at 5 kPa
entropyList5 = [0.0001, 0.2954, 0.5705, 0.8287, 1.0723, 1.3034, 1.5236, 1.7344, 1.9374, 2.1338, 2.3251, 2.5127, 2.6983, 2.8841] #list of entropys at 5 kPa
volumeList10 = [0.0009952, 0.0009973, 0.0010035, 0.0010127, 0.0010244, 0.0010385, 0.0010549, 0.0010738, 0.0010954, 0.0011200, 0.0011482, 0.0011809, 0.0012192, 0.0012653] #list of volumes at 10 kPa
energyList10 = [0.12, 83.31, 166.33, 249.43, 332.69, 416.23, 500.18, 584.72, 670.06, 756.48, 844.32, 934.01, 1026.2, 1121.6] #list of internal energys at 10 kPa
enthalpyList10 = [10.07, 93.28, 176.37, 259.55, 342.94, 426.62, 510.73, 595.45, 681.01, 767.68, 855.8, 945.82, 1038.3, 1134.3] #list of enthalpys at 10 kPa
entropyList10 = [0.0003, 0.2943, 0.5685, 0.826, 1.0691, 1.2996, 1.5191, 1.7293, 1.9316, 2.1271, 2.3174, 2.5037, 2.6876, 2.871] #list of entropys at 10 kPa
userVal = 0 #users inputed temperature
userPressure = 0 #users inputed pressure
outputs = [] #a list of the four calculated values

# Prompt user for Temperature and pressure
# Store it in a variable
userVal = float(input("Enter a temperature between 0 and 260 deg C: "))
userPressure = float(input("Enter a pressure between 5 and 10 MPa: "))

# Make sure temperature and pressure is in bounds
# Check if it is below the min or above the max
# If it is, reprompt the user for data until it is in range
while(userVal > 260 or userVal < 0):
    userVal = float(input("That temperature is not between 0 and 260 degrees C.\nPlease enter a valid temperature: "))

while(userPressure > 10 or userPressure < 5):
    userPressure = float(input("That pressure is not between 5 and 10 MPa\nPlease enter a valid pressure: "))


#################################
####### PROCESS USER DATA #######
###### WILLIAM AND HENRY ########

# Locate the range the user data falls between
# Go through each value in the list until the input is greater than a value, then that value and the next are the bounds

minIndex = 13
for i in tempList:
    if i > userVal:
        minIndex = tempList.index(i) - 1
        break

maxIndex = minIndex + 1

# Get an intropolation function for each range
# Find the change in temperature between user data and the lowest range
# Find slope between the range values

def slopeFunc(minIndex, maxIndex):
    slopeList = []
    m = (volumeList5[maxIndex] - volumeList5[minIndex])/(tempList[maxIndex]-tempList[minIndex])
    slopeList.append(m)
    m = (energyList5[maxIndex] - energyList5[minIndex])/(tempList[maxIndex]-tempList[minIndex])
    slopeList.append(m)
    m = (enthalpyList5[maxIndex] - enthalpyList5[minIndex])/(tempList[maxIndex]-tempList[minIndex])
    slopeList.append(m)
    m = (entropyList5[maxIndex] - entropyList5[minIndex]) / (tempList[maxIndex]-tempList[minIndex])
    slopeList.append(m)

    return slopeList

# Calculate values based off of the intropolation function
# Return a list containing each calculated value

def interpolate5(actualTemp, minIndex, maxIndex):
    mList = slopeFunc(minIndex, maxIndex)
    propertiesList = []

    x = mList[0] * (actualTemp - tempList[minIndex]) + volumeList5[minIndex]
    propertiesList.append(x)

    x = mList[1] * (actualTemp - tempList[minIndex]) + energyList5[minIndex]
    propertiesList.append(x)

    x = mList[2] * (actualTemp - tempList[minIndex]) + enthalpyList5[minIndex]
    propertiesList.append(x)

    x = mList[3] * (actualTemp - tempList[minIndex]) + entropyList5[minIndex]
    propertiesList.append(x)

    return propertiesList


def interpolate10(actualTemp, minIndex, maxIndex):
    mList = slopeFunc(minIndex, maxIndex)
    propertiesList = []

    x = mList[0] * (actualTemp - tempList[minIndex]) + volumeList10[minIndex]
    propertiesList.append(x)

    x = mList[1] * (actualTemp - tempList[minIndex]) + energyList10[minIndex]
    propertiesList.append(x)

    x = mList[2] * (actualTemp - tempList[minIndex]) + enthalpyList10[minIndex]
    propertiesList.append(x)

    x = mList[3] * (actualTemp - tempList[minIndex]) + entropyList10[minIndex]
    propertiesList.append(x)

    return propertiesList


##### EXTRA CREDIT #######
######## WILLIAM #########

def newInterpolate(actualPressure):

    # Get the four values at kPa = 5 and 10
    values1 = interpolate5(userVal, minIndex, maxIndex)
    values2 = interpolate10(userVal, minIndex, maxIndex)

    # For each value, interpolate the four values using pressure as the x axis
    # and the values as the y axis between kPa = 5 and 10
    newVolumeSlope = (values2[0] - values1[0]) / 5
    newVolume = newVolumeSlope * (actualPressure - 5) + values1[0]

    newEnergySlope = (values2[1] - values1[1]) / 5
    newEnergy = newEnergySlope * (actualPressure - 5) + values1[1]

    newEnthalpySlope = (values2[2] - values1[2]) / 5
    newEnthalpy = newEnthalpySlope * (actualPressure - 5) + values1[2]

    newEntropySlope = (values2[3] - values1[3]) / 5
    newEntropy = newEntropySlope * (actualPressure - 5) + values1[3]

    # Return the four in the order they will be printed
    return [newVolume, newEnergy, newEnthalpy, newEntropy]



#################################
#### FORMAT/OUTPUT USER DATA ####
########### HENRY ###############

# Print the calculated volume to 7 decimal places
valuesinterpolate = newInterpolate(userPressure)
print('Properties at', userVal,'deg C and', userPressure, 'MPa are:')
print('Specific volume (m^3/kg): {}'.format(round(valuesinterpolate[0], 7)))

# Print the internal energy to 2 decimal places
print('Specific internal energy (kJ/kg): {}'.format(round(valuesinterpolate[1], 2)))

# Print the calculated enthalpy to 2 decimal places
print('Specific enthalpy (kJ/kg): {}'.format(round(valuesinterpolate[2], 2)))

# Print the calculated entropy to 4 decimal places
print('Specific entropy (kJ/kgK): {}'.format(round(valuesinterpolate[3], 4)))
