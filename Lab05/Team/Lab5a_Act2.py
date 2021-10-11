# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab 5a-2
# Date:         27 9 2021
#

#FIRST TASK: Collect all the types of data we need to calculate risk using the input() function.
#'m', '77', 'n', '281', '45', '155', 'y']
# Sex (M/F)
sex = input("Enter your sex (M/F): ").capitalize()
# Age (years)
age = float(input("Enter your age (years): "))
# Smoker (Y/N)
smoker = input("Do you smoke cigarettes (Y/N)? ").capitalize()
# Total cholesterol (mg/dL)
totalCholesterol = float(input("Enter your total cholesterol (mg/dL): "))
# HDL cholesterol (mg/dL)
hdlCholesterol = float(input("Enter your HDL cholesterol (mg/dL): "))
# Systolic BP (mmHg)
systolicBP = float(input("Enter your systolic BP (mmHg): "))
# Taking blood pressure medication (Y/N)
takingBPMeds = input("Are you taking blood pressure medication (Y/N)? ").capitalize()

heartAttackPoints = 0

#SECOND TASK: Create a sequence of steps that you will follow

# TODO: check any out of bounds variables
if( not( 20 <= age <= 8)):
    # Check elif Male or Female
    if (sex == "M"):
        # Depending on M or F, check age and add corresponding score
        if (20 <= age <= 34):
            heartAttackPoints += -9
        elif (35 <= age <= 39):
            heartAttackPoints += -4
        elif (40 <= age <= 44):
            heartAttackPoints += 0
        elif (45 <= age <= 49):
            heartAttackPoints += 3
        elif (50 <= age <= 54):
            heartAttackPoints += 6
        elif (55 <= age <= 59):
            heartAttackPoints += 8
        elif (60 <= age <= 64):
            heartAttackPoints += 10
        elif (65 <= age <= 69):
            heartAttackPoints += 11
        elif (70 <= age <= 74):
            heartAttackPoints += 12
        elif (75 <= age <= 79):
            heartAttackPoints += 13

        # Check total cholesterol and depending on age add corresponding score
        if (totalCholesterol < 160):
            if (20 <= age <= 39):
                heartAttackPoints += 0
            elif (40 <= age <= 49):
                heartAttackPoints += 0
            elif (50 <= age <= 59):
                heartAttackPoints += 0
            elif (60 <= age <= 69):
                heartAttackPoints += 0
            elif (70 <= age <= 79):
                heartAttackPoints += 0

        elif (160 <= totalCholesterol <= 199):
            if (20 <= age <= 39):
                heartAttackPoints += 4
            elif (40 <= age <= 49):
                heartAttackPoints += 3
            elif (50 <= age <= 59):
                heartAttackPoints += 2
            elif (60 <= age <= 69):
                heartAttackPoints += 1
            elif (70 <= age <= 79):
                heartAttackPoints += 0

        elif (200 <= totalCholesterol <= 239):
            if (20 <= age <= 39):
                heartAttackPoints += 7
            elif (40 <= age <= 49):
                heartAttackPoints += 5
            elif (50 <= age <= 59):
                heartAttackPoints += 3
            elif (60 <= age <= 69):
                heartAttackPoints += 1
            elif (70 <= age <= 79):
                heartAttackPoints += 0

        elif (240 <= totalCholesterol <= 279):
            if (20 <= age <= 39):
                heartAttackPoints += 9
            elif (40 <= age <= 49):
                heartAttackPoints += 6
            elif (50 <= age <= 59):
                heartAttackPoints += 4
            elif (60 <= age <= 69):
                heartAttackPoints += 2
            elif (70 <= age <= 79):
                heartAttackPoints += 1

        elif (totalCholesterol >= 280):
            if (20 <= age <= 39):
                heartAttackPoints += 11
            elif (40 <= age <= 49):
                heartAttackPoints += 8
            elif (50 <= age <= 59):
                heartAttackPoints += 5
            elif (60 <= age <= 69):
                heartAttackPoints += 3
            elif (70 <= age <= 79):
                heartAttackPoints += 1
        # Check elif smoker or nonsmoker and add corresponding score for age and sex
        if (smoker == "N"):
            heartAttackPoints += 0
        elif (smoker == "Y"):
            if (20 <= age <= 39):
                heartAttackPoints += 8
            elif (40 <= age <= 49):
                heartAttackPoints += 5
            elif (50 <= age <= 59):
                heartAttackPoints += 3
            elif (60 <= age <= 69):
                heartAttackPoints += 1
            elif (70 <= age <= 79):
                heartAttackPoints += 1
        # Check HDL cholesterol and add corresponding score
        if (hdlCholesterol >= 60):
            heartAttackPoints -= 1
        elif (50 <= hdlCholesterol <= 59):
            heartAttackPoints += 0
        elif (40 <= hdlCholesterol <= 49):
            heartAttackPoints += 1
        elif (hdlCholesterol < 40):
            heartAttackPoints += 2
        # Check systolic blood pressure and based on elif treated or not assign points based on this
        if (takingBPMeds == "N"):
            if (systolicBP < 120):
                heartAttackPoints += 0
            elif (120 <= systolicBP <= 129):
                heartAttackPoints += 0
            elif (130 <= systolicBP <= 139):
                heartAttackPoints += 1
            elif (140 <= systolicBP <= 159):
                heartAttackPoints += 1
            elif (systolicBP >= 160):
                heartAttackPoints += 2
        else:
            if (systolicBP < 120):
                heartAttackPoints += 0
            elif (120 <= systolicBP <= 129):
                heartAttackPoints += 1
            elif (130 <= systolicBP <= 139):
                heartAttackPoints += 2
            elif (140 <= systolicBP <= 159):
                heartAttackPoints += 2
            elif (systolicBP >= 160):
                heartAttackPoints += 3

        percentRisk = -1
        if (heartAttackPoints < 0):
            percentRisk = 0
        elif (0 <= heartAttackPoints <= 4):
            percentRisk = 1
        elif (5 <= heartAttackPoints <= 6):
            percentRisk = 2
        elif (heartAttackPoints == 7):
            percentRisk = 3
        elif (heartAttackPoints == 8):
            percentRisk = 4
        elif (heartAttackPoints == 9):
            percentRisk = 5
        elif (heartAttackPoints == 10):
            percentRisk = 6
        elif (heartAttackPoints == 11):
            percentRisk = 8
        elif (heartAttackPoints == 12):
            percentRisk = 10
        elif (heartAttackPoints == 13):
            percentRisk = 12
        elif (heartAttackPoints == 14):
            percentRisk = 16
        elif (heartAttackPoints == 15):
            percentRisk = 20
        elif (heartAttackPoints == 16):
            percentRisk = 25
        elif (17 <= heartAttackPoints):
            percentRisk = 30
    else:
        # Depending on M or F, check age and add corresponding score
        if (20 <= age <= 34):
            heartAttackPoints += -7
        elif (35 <= age <= 39):
            heartAttackPoints += -3
        elif (40 <= age <= 44):
            heartAttackPoints += 0
        elif (45 <= age <= 49):
            heartAttackPoints += 3
        elif (50 <= age <= 54):
            heartAttackPoints += 6
        elif (55 <= age <= 59):
            heartAttackPoints += 8
        elif (60 <= age <= 64):
            heartAttackPoints += 10
        elif (65 <= age <= 69):
            heartAttackPoints += 12
        elif (70 <= age <= 74):
            heartAttackPoints += 14
        elif (75 <= age <= 79):
            heartAttackPoints += 16

        # Check total cholesterol and depending on age add corresponding score
        if (totalCholesterol < 160):
            if (20 <= age <= 39):
                heartAttackPoints += 0
            elif (40 <= age <= 49):
                heartAttackPoints += 0
            elif (50 <= age <= 59):
                heartAttackPoints += 0
            elif (60 <= age <= 69):
                heartAttackPoints += 0
            elif (70 <= age <= 79):
                heartAttackPoints += 0

        elif (160 <= totalCholesterol <= 199):
            if (20 <= age <= 39):
                heartAttackPoints += 4
            elif (40 <= age <= 49):
                heartAttackPoints += 3
            elif (50 <= age <= 59):
                heartAttackPoints += 2
            elif (60 <= age <= 69):
                heartAttackPoints += 1
            elif (70 <= age <= 79):
                heartAttackPoints += 1

        elif (200 <= totalCholesterol <= 239):
            if (20 <= age <= 39):
                heartAttackPoints += 8
            elif (40 <= age <= 49):
                heartAttackPoints += 6
            elif (50 <= age <= 59):
                heartAttackPoints += 4
            elif (60 <= age <= 69):
                heartAttackPoints += 2
            elif (70 <= age <= 79):
                heartAttackPoints += 1

        elif (240 <= totalCholesterol <= 279):
            if (20 <= age <= 39):
                heartAttackPoints += 11
            elif (40 <= age <= 49):
                heartAttackPoints += 8
            elif (50 <= age <= 59):
                heartAttackPoints += 5
            elif (60 <= age <= 69):
                heartAttackPoints += 3
            elif (70 <= age <= 79):
                heartAttackPoints += 2

        elif (totalCholesterol >= 280):
            if (20 <= age <= 39):
                heartAttackPoints += 13
            elif (40 <= age <= 49):
                heartAttackPoints += 10
            elif (50 <= age <= 59):
                heartAttackPoints += 7
            elif (60 <= age <= 69):
                heartAttackPoints += 4
            elif (70 <= age <= 79):
                heartAttackPoints += 2
        # Check elif smoker or nonsmoker and add corresponding score for age and sex
        if (smoker == "N"):
            heartAttackPoints += 0
        elif (smoker == "Y"):
            if (20 <= age <= 39):
                heartAttackPoints += 9
            elif (40 <= age <= 49):
                heartAttackPoints += 7
            elif (50 <= age <= 59):
                heartAttackPoints += 4
            elif (60 <= age <= 69):
                heartAttackPoints += 2
            elif (70 <= age <= 79):
                heartAttackPoints += 1
        # Check HDL cholesterol and add corresponding score
        if (hdlCholesterol >= 60):
            heartAttackPoints -= 1
        elif (50 <= hdlCholesterol <= 59):
            heartAttackPoints += 0
        elif (40 <= hdlCholesterol <= 49):
            heartAttackPoints += 1
        elif (hdlCholesterol < 40):
            heartAttackPoints += 2
        # Check systolic blood pressure and based on elif treated or not assign points based on this
        if (takingBPMeds == "N"):
            if (systolicBP < 120):
                heartAttackPoints += 0
            elif (120 <= systolicBP <= 129):
                heartAttackPoints += 1
            elif (130 <= systolicBP <= 139):
                heartAttackPoints += 2
            elif (140 <= systolicBP <= 159):
                heartAttackPoints += 3
            elif (systolicBP >= 160):
                heartAttackPoints += 4
        else:
            if (systolicBP < 120):
                heartAttackPoints += 0
            elif (120 <= systolicBP <= 129):
                heartAttackPoints += 3
            elif (130 <= systolicBP <= 139):
                heartAttackPoints += 4
            elif (140 <= systolicBP <= 159):
                heartAttackPoints += 5
            elif (systolicBP >= 160):
                heartAttackPoints += 6
    # Check the final total score and return the %risk for the person based on the point total that they had.
        percentRisk = -1
        if (heartAttackPoints < 9):
            percentRisk = 0
        elif (9 <= heartAttackPoints <= 12):
            percentRisk = 1
        elif (heartAttackPoints == 13 or heartAttackPoints == 14):
            percentRisk = 2
        elif (heartAttackPoints == 15):
            percentRisk = 3
        elif (heartAttackPoints == 16):
            percentRisk = 4
        elif (heartAttackPoints == 17):
            percentRisk = 5
        elif (heartAttackPoints == 18):
            percentRisk = 6
        elif (heartAttackPoints == 19):
            percentRisk = 8
        elif (heartAttackPoints == 20):
            percentRisk = 11
        elif (heartAttackPoints == 21):
            percentRisk = 14
        elif (heartAttackPoints == 22):
            percentRisk = 17
        elif (heartAttackPoints == 23):
            percentRisk = 22
        elif (heartAttackPoints == 24):
            percentRisk = 27
        elif (heartAttackPoints >= 25):
            percentRisk = 30

    if (percentRisk == 0):
        print("Your 10-year risk of a heart attack is <1%")
    elif (percentRisk == 30):
        print("Your 10-year risk of a heart attack is >30%")
    else:
        print("Your 10-year risk of a heart attack is", str(percentRisk) + "%")
else:
    print("Not within range")