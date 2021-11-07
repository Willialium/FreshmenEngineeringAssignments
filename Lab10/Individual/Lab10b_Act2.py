# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         William Taylor
# Section:      209
# Assignment:   Lab10b-Act2
# Date:         6 11 2021
#

fileName = input("Please enter the output filename: ")
pAmnt = float(input("Please enter the principal amount: "))
months = int(input("Please enter the term length (months): "))
iRate = float(input("Please enter the annual interest rate: "))
accurInterest = 0
interest = 0
mPayment = (pAmnt * iRate / 12) / (1 - (1 / (1 + iRate / 12)) ** months)
loanBalance = pAmnt

with open(fileName + ".txt", 'w') as file:
    file.write('Month,Total Accrued,Loan Balance\n')
    for i in range(0, months+1):

        # Prints the values to the screen
        file.write(str(i) + ',')
        file.write("${:.2f},".format(accurInterest))
        file.write("${:.2f}\n".format(loanBalance))

        # calculates the interest for that month based off the current balance
        interest = loanBalance * iRate / 12

        # adds the interest to a running total of the interest accrued
        accurInterest += interest

        # calculates the new loan balance
        loanBalance = loanBalance + interest - mPayment







