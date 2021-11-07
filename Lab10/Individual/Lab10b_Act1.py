# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   Lab10b-1
# Date:         6 11 2021
#

# Opens the file
with open('game.txt', 'r') as file:
    # Creates a list of the file
    lines = file.readlines()
    index = 0
    coins = 0
    open('coins.txt', 'w').write('') # Emptys the file

    while index != len(lines):     # Until the pointer is right after the last line
        values = lines[index].split(' ')
        if (values[1][-1] == '\n'): # Clears the newline
            values[1] = values[1][:-1]
        number = int(values[1]) # Gets the number

        if(values[0] == 'coin'): # If it is coin, increase the pointer by one and the coin total by one
            coins += number
            index += 1
            with open('coins.txt', 'a') as coinFile:
                coinFile.write(str(number) + '\n')
        elif(values[0] == 'jump'): # if it is jump, change the pointer by the number
            index += number
        else: # otherwise increase the pointer by 1
            index += 1

    # print the total coins
    print("Total coins:", coins)