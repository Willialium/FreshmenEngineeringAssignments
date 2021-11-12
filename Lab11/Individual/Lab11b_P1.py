# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   Lab 11b-P1
# Date:         10 11 2021
#

# The function which takes the three lists
def least_profitable(names, cost, value):
    if len(names) == 0:  # If the lists are empty, return empty and 0
        return 'Empty', 0
    lowest = float(value[0]) - float(cost[0])  # Get a starting min value
    index = 0

    for i in range(len(names)):  # For every index in each list,
        if float(value[i]) - float(cost[i]) < lowest:  # If the value - cost is less than the current lowest,
            lowest = float(value[i]) - float(cost[i])  # Set that to the new lowest and save the index
            index = i

    return names[index], float(lowest)  # Return the name along with the calculated profit


# TEST CASES
test1 = [['nameOne', 'nameTwo', 'nameThree'], [0, 10, 5], [10, 11, 16]]
test2 = [['nameOne'], [10], [5]]
test3 = [[], [], []]
test4 = [['nameOne', 'nameTwo', 'nameThree'], ['0', '10', '5'], ['10', '11', '16']]

# PRINTING RESULTS OF TEST CASES
print('Calling the function with lists {}, {}, and {} returns {}'
      .format(test1[0], test1[1], test1[2], least_profitable(test1[0], test1[1], test1[2])))
print('Calling the function with lists {}, {}, and {} returns {}'
      .format(test2[0], test2[1], test2[2], least_profitable(test2[0], test2[1], test2[2])))
print('Calling the function with lists {}, {}, and {} returns {}'
      .format(test3[0], test3[1], test3[2], least_profitable(test3[0], test3[1], test3[2])))
print('Calling the function with lists {}, {}, and {} returns {}'
      .format(test4[0], test4[1], test4[2], least_profitable(test4[0], test4[1], test4[2])))