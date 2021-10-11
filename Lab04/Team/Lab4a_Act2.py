# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab 4-2
# Date:         24 9 2021
#

A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

equation = "The quadratic equation is "

# If there is no A value
if(A != 0):
    if(A < 0):
        equation += "- "
    if(abs(A)!=1):
        equation+=str(abs(A))
    equation += "x^2 "

# If there is an A value and no B value
if(B != 0):
    if(B > 0):
        if A != 0:
            equation += "+ "
    else:
        equation += "- "
    if(abs(B)!=1):
        equation+=str(abs(B))
    equation += "x "

# If there is an A and B value but no C value
if(C != 0):
    if(C > 0 and B != 0):
        equation += "+ "
    else:
        equation += "- "
    equation+=str(abs(C)) + " "

equation += "= 0"

# Print the equation
print(equation)
