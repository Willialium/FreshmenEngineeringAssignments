def getData(timeList, disList):
        resultList = []

        for i in range(1, len(timeList)):
            vel = (disList[i] - disList[i-1]) / (timeList[i] - timeList[i-1])
            resultList.append(vel)

        return resultList

test1 = getData([0,1,2,3], [0,2,4,6])
test2 = getData([-1,0,1,2], [0,2,4,6])
test3 = getData([0,1,2,3], [-2,0,2,4])
test4 = getData([1,44,81], [-2, 4.56, 20])
#test5 = getData(['1', 5], [5, 7]) # Error

print('For times {} and distances {}, the function returns {}'.format([0,1,2,3], [0,2,4,6], getData([0,1,2,3], [0,2,4,6])))
print('For times {} and distances {}, the function returns {}'.format([-1,0,1,2], [0,2,4,6], getData([-1,0,1,2], [0,2,4,6])))
print('For times {} and distances {}, the function returns {}'.format([0,1,2,3], [-2,0,2,4], getData([0,1,2,3], [-2,0,2,4])))
print('For times {} and distances {}, the function returns {}'.format([1,44,81], [-2, 4.56, 20], getData([1,44,81], [-2, 4.56, 20])))


