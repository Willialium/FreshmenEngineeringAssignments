# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   Lab 11b-P3
# Date:         10 11 2021
#

# The function that takes in a number
def isPerfect(number):
    divisors = []  # List containing the divisors

    for divisor in range(1, int(number)):  # For every number between 1 and the number
        if number % divisor == 0:  # If that number is a divisor, add it to the list
            divisors.append(divisor)

    # If the number is a positive integer and the sum of its divisors equals the number, return True
    # Else return False
    return (number > 0) and (sum(divisors) == number) and (number == int(number))


# TEST CASES
print('If 1 is passed through the function, it returns', isPerfect(1))
print('If 6 is passed through the function, it returns', isPerfect(6))
print('If 10 is passed through the function, it returns', isPerfect(10))
print('If 0 is passed through the function, it returns', isPerfect(0))
print('If -5 is passed through the function, it returns', isPerfect(-5))
print('If 12.5 is passed through the function, it returns', isPerfect(12.5))