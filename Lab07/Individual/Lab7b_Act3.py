# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   7b-2b
# Date:         12-10-2021
#

vectorA_Values = input("Enter the elements for vector A: ").split(" ") # Gets the vector elements and converts to a list
vectorB_Values = input("Enter the elements for vector B: ").split(" ")
vectorA_Values = [float(i) for i in vectorA_Values]  # Converts the list to a list of ints
vectorB_Values = [float(i) for i in vectorB_Values]


# Adds the square of each value in a Vector, and the takes the square root of the sum

# For vector A
magnitudeA = 0
for element in vectorA_Values:
    magnitudeA += element**2
magnitudeA = magnitudeA**(1/2)
print("The magnitude of vector A is {:.4f}".format(magnitudeA))

# For Vector B
magnitudeB = 0
for element in vectorB_Values:
    magnitudeB += element**2
magnitudeB = magnitudeB**(1/2)
print("The magnitude of vector B is {:.4f}".format(magnitudeB))


# Creates a list who's components are the sum of each corresponding element in Vector A and B
sumVector = []
for i in range(len(vectorA_Values)):
    sumVector.append(vectorA_Values[i] + vectorB_Values[i])
print("A + B is", sumVector)

# Creates a list who's components are the difference of each corresponding element in Vector A and B
difVector = []
for i in range(len(vectorA_Values)):
    difVector.append(vectorA_Values[i] - vectorB_Values[i])
print("A - B is", difVector)

# Gets the sum of the product each corresponding value in Vector A and B
dotProduct = 0
for i in range(len(vectorA_Values)):
    dotProduct += vectorA_Values[i] * vectorB_Values[i]
print("The dot product is", dotProduct)