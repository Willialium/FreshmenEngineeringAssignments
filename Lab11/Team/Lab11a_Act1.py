def findVals(dataList):
    mini = 0
    maxi = 0
    average = 0

    # Makes sure that there is at least one value in the list
    if len(dataList) != 0:
        mini = min(dataList)
        maxi = max(dataList)
        average = sum(dataList) / len(dataList)

    return mini, maxi, average

test1 = [1,2,3,4] # min = 1, max = 4, average = 2.5
test2 = [-2,-1,0,1,2] # min = -2, max = 2, average = 0
test3 = [3,3,3] # min = 3, max = 3, average = 3
test4 = [4] # min = 4, max = 4, average = 4
test5 = [] # doesn't work

print('The min, max, and average of {} is {}'.format(test1, findVals(test1)))
print('The min, max, and average of {} is {}'.format(test2, findVals(test2)))
print('The min, max, and average of {} is {}'.format(test3, findVals(test3)))
print('The min, max, and average of {} is {}'.format(test4, findVals(test4)))
print('The min, max, and average of {} is {}'.format(test5, findVals(test5)))