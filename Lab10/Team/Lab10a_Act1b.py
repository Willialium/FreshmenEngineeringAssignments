# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab10a-1b
# Date:         5 11 2021
#

# Checks if each term is defined in a passport
def valid(thisList):
    thisStr = ''
    for data in thisList:
        thisStr += data + ' '
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in keys:
        if key not in thisStr:
            return False
    return validValues(thisList)


# Checks if each defined term has valid data
def validValues(thisList):
    isValid = True
    for data in thisList:
        splitData = data.split(':')  # code, value
        try:
            if splitData[0] == 'byr':
                year = float(splitData[1])
                if 2005 < year or year < 1920 or year % 1 != 0:
                    isValid = False
            elif splitData[0] == 'iyr':
                year = float(splitData[1])
                if 2021 < year or year < 2011 or year % 1 != 0:
                    isValid = False
            elif splitData[0] == 'eyr':
                year = float(splitData[1])
                if 2031 < year or year < 2021 or year % 1 != 0:
                    isValid = False
            elif splitData[0] == 'hgt':
                value = float(splitData[1][:-2])
                unit = splitData[1][-2:]
                if unit == 'cm':
                    if 193 < value or value < 150:
                        isValid = False
                elif unit == 'in':
                    if 76 < value or value < 59:
                        isValid = False
                else:
                    isValid = False
            elif splitData[0] == 'hcl':
                checkList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
                if splitData[1][0] != '#':
                    isValid = False
                elif len(splitData[1][1:]) != 6:
                    isValid = False
                for char in splitData[1][1:]:
                    if char not in checkList:
                        isValid = False
            elif splitData[0] == 'ecl':
                checkList = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if splitData[1] not in checkList:
                    isValid = False
            elif splitData[0] == 'pid':
                if len(splitData[1]) != 9:
                    isValid = False
                value = int(splitData[1])
        except:
            isValid = False

    return isValid


# Creates a dictionary of each passport and its formatting to print to the file
total = {}
format = {}
with open('Lab9a_input.txt', 'r') as file:
    text = file.readlines()
    temp = []
    counter = 0
    format[0] = []
    for line in text:
        if (line != '\n'):
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
    for i in range(len(total) - 1, -1, -1):
        if not valid(total[i]):
            total.pop(i)
            format.pop(i)
    print('There are', len(total), 'valid passports')

# prints to the file
with open('Lab10a_Act1b_valid.txt', 'a') as validFile:
    open('Lab10a_Act1b_valid.txt', 'w').write('')
    for key in total:
        for index in range(len(total[key])):
            validFile.write(total[key][index] + format[key][index])
        validFile.write('\n')
