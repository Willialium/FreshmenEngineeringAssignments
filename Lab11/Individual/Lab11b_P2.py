# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   Lab 11b-P2
# Date:         10 11 2021
#

# Takes the required parameters, making the second address line optional
def printAddress(name, city, state, zipCode, address, address2=''):
    print(name)
    print(address)
    if(address2 != ''): # If there was a second address entered, print it
        print(address2)
    print('{}, {}  {}'.format(city, state, zipCode)) # Print instead of return


# TEST CASES
print('With name: Chewbacca, city: Millenium Falcon, state: TX, zip code: 77777, and address 100 Teddy Bear Lane,')
print('The function prints:')
printAddress('Chewbacca', 'Millenium Falcon', 'TX', '77777', '100 Teddy Bear Lane')
print()
print('With name: Tony Stark, city: New York, state: NY, zip code: 33333, and address 300 Avenger Way and Apartment 1,')
print('The function prints:')
printAddress('Tony Stark', 'New York', 'NY', '33333', '300 Avenger Way', 'Apartment 1')
