# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab 6a-2
# Date:         4 10 2021
#

totalPrimes = 0
for i in range(2, 101):
    divisor = 2
    while(i % divisor != 0 and i!=divisor):
        divisor += 1
    if(divisor == i):
        print("{} is prime".format(i))
        totalPrimes += 1
    else:
        print("{} is not prime".format(i))

print("\nThere are {} prime numbers between 2 and 100".format(totalPrimes))