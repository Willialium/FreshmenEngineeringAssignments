# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   Lab 5b-1
# Date:         30 9 2021
#


# Create a slope equation for each section
# Create a function that returns stress given strain for each section using the slope formula
pointA = [.01, 43]
pointC = [.06, 43.5]
pointD = [.18, 60]
pointE = [.27, 51]


def stress0A(strain):
    slope = pointA[1] / pointA[0]
    return strain * slope


def stressAC(strain):
    slope = (pointC[1] - pointA[1]) / (pointC[0] - pointA[0])
    yIntercept = (slope * -pointA[0]) + pointA[1]
    return strain * slope + yIntercept


def stressCD(strain):
    slope = (pointD[1] - pointC[1]) / (pointD[0] - pointC[0])
    yIntercept = (slope * -pointC[0]) + pointC[1]
    return strain * slope + yIntercept


def stressDE(strain):
    slope = (pointE[1] - pointD[1]) / (pointE[0] - pointD[0])
    yIntercept = (slope * -pointD[0]) + pointD[1]
    return strain * slope + yIntercept


# Get user input
strainInput = float(input("Enter the strain: "))
stress = 0

# If input is outside of the range, return an error
if 0 <= strainInput <= .27:

    # Check if input is between 0-A, A-C, C-D, or D-E
    # Depending on where the input is, call the method that correlates with that domain
    if 0 <= strainInput <= .01:
        stress = stress0A(strainInput)
    elif .01 < strainInput <= .06:
        stress = stressAC(strainInput)
    elif .06 < strainInput <= .18:
        stress = stressCD(strainInput)
    elif .18 < strainInput <= .27:
        stress = stressDE(strainInput)

        # Print the stress approximation to the screen
    print("The stress is approximately {:.1f}".format(stress))
else:
    print("Strain is undefined in that region")
