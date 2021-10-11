# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab 4-3
# Date:         24 9 2021
#

########### Part A ###########
# Converts user input into a boolean
def toBool(bool):
    trueList = ["t", "T", "True"]
    falseList = ["f", "F", "False"]

    if bool in trueList:
        return True
    elif bool in falseList:
        return False
    return bool


# gets booleans a b and c
a = toBool(input("Enter True or False for a: "))
b = toBool(input("Enter True or False for b: "))
c = toBool(input("Enter True or False for c: "))

########### Part B ###########

# Evaluates the printed if statements
print("a and b and c:", a and b and c)
print("a or b or c:", a or b or c)

########### Part C ###########

# Evaluates a XOR b
print("XOR:", a != b)

# prints if there is an ODD number of Trues
print("Odd number:", (a == b) == c)

########### Part D ###########


complex1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
complex2 = (not ((b or not c) and (not a or not c))) or \
           (not (c or not (b and c))) or (a and not c) and \
           (not a or (a and b and c) or (a and ((b and not c) or (not b))))

simple1 = not b or (not a and not c)
simple2 = a or not b and c

print("Complex 1:", complex1)
print("Complex 2:", complex2)
print("Simple 1:", simple1)
print("Simple 2:", simple2)
