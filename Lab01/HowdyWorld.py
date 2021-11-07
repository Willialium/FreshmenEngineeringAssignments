import csv

with open('file.csv', 'w',newline='') as file:
    sheetReader = csv.writer(file, delimiter=',')
    sheetReader.writerows([[1,2,3],[4,5,6]])