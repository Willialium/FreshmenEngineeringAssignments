# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   Lab10b-3
# Date:         6 11 2021
#

import csv

with open('CLLWeatherData.csv', 'r') as csvFile:

    # Creating variables
    sheet_reader = csv.reader(csvFile, delimiter=',')
    totalPrecipitation = 0
    maxTempList = []
    minTempList = []
    total = 0
    rows = [row for row in sheet_reader]
    monthList = ['January', 'February', 'March', 'April', 'May', 'June', # For determining the date
                 'July', 'August', 'September', 'October', 'November', "December"]

    # Creates the list of the data
    for row in rows:
        if row[0] == 'Date': # Skips the first row
            continue
        maxTempList.append(float(row[4]))
        minTempList.append(float(row[5]))
        totalPrecipitation += float(row[2])
        total += 1
    totalPrecipitation /= total

    # Calculates the answers
    print('3-year maximum temperature: {} F'.format(int(max(maxTempList))))
    print('3-year minimum temperature: {} F'.format(int(min(minTempList))))
    print('3-year average precipitation: {:.3f} inches'.format(totalPrecipitation))

    # Gets data from the user
    userMonth = monthList.index(input('\nPlease enter a month: ')) + 1
    userYear = input('Please enter a year: ')

    # Gets the information for the day based off the users input
    month = []
    for row in rows[1:]:
        date = row[0].split('/')
        if (int(date[0]) == userMonth) and (date[2] == userYear):
            month.append(row)

    # Calculates the data
    tempList = []
    windSpeed = []
    precipitations = []
    for day in month:
        tempList.append(float(day[3]))
        precipitations.append(float(day[2]))
        if float(day[1]) > 10:
            windSpeed.append(float(day[1]))

    # Prints the data to the screen
    print('\nFor {} {}:'.format(monthList[userMonth-1], userYear))
    print('Mean daily temperature: {:.1f} F'.format(sum(tempList) / len(month)))
    print('Percentage of days with average wind speed above 10 mph: {:.1f}%'.format(100 * len(windSpeed) / len(month)))
    print('Mean daily precipitation: {:.4f} inches'.format(sum(precipitations) / len(month)))

