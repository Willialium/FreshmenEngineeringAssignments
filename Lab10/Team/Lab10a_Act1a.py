# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab 10a-1
# Date:         5 11 2021
#

# Checks if each item is defined in a passport
def valid(thisList):
    thisStr = ''
    for data in thisList:
        thisStr += data + ' '
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in keys:
        if key not in thisStr:
            return False
    return True

# Creates a dictionary of each passport and its formatting to print to the file
total = {}
format = {}
with open('Lab9a_input.txt', 'r') as file:
    temp = []
    counter = 0
    format[0] = []
    text = file.readlines()
    for line in text:
        if(line != '\n'):
            temp += line.split(' ')
            for data in line.split(' ')[:-1]:
                format[counter].append(' ')
            format[counter].append('\n')
            temp[-1] = temp[-1][:-1]
        else:
            format[counter].append('\n')
            total[counter] = temp
            counter += 1
            temp = []
            format[counter] = []

    temp[-1] = text[-1].split(' ')[-1]
    total[counter] = temp


    totalValid = 0
    for i in range(len(total)-1, -1, -1):
        if not valid(total[i]):
            total.pop(i)
            format.pop(i)
    print('There are',len(total),'valid passports')


#prints to the file
with open('Lab10a_Act1a_valid.txt', 'a') as validFile:
    open('Lab10a_Act1a_valid.txt', 'w').write('')
    for key in total:
        for index in range(len(total[key])):
            validFile.write(total[key][index] + format[key][index])
        validFile.write('\n')