# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab12-PartC
# Date:         19-11-2021
#


###### GAME #####
# Text based pokemon based game

### VARIABLES ###
# caughtPkmn dict - dictionary with the key as the index and the value as the name
# AllPkmn dict - dictionary with the key as the index and the value as the name
# Total candy
# userName

### FUNCTIONS ###
def getInput():
    '''Gets a input from a user and either returns the int option or quit. Reprompts the user if they input something else'''
    pass
# tries to get the users number for selecting
# If they dont input a number but it is equal to quit, return quit
# if not, prompt them to enter a number until they enter a number
# Return the number
def readFile():
    '''Reads the pokemon CSV file to create the allPkmn dictionary'''
    pass
# Creates the allPkmn dictionary where the key is the pokemon's index and the value is a list containing the name, min CP, max CP

def getUser(userName):
    '''Reads the user file and initializes all the variables according to the user's saved data'''
    pass
# Reads the user file to get each of the users
# Each line will start with the name of the user.total candy followed by the index of the pokemon.level
# For example, for user Name a line will look like:
# Name.20 1.1 5.1
# the userName will be set to userName
# Each pokemon will be added to the pokemon list
# The total candy variable will be set to the users candy

def mainMenu():
    '''Gives the user the option to fight, view, or level up their pokemon using the getInput to get their input and calling the corresponding function they choose'''
    pass
# Gives the user options to select their profile to create a new profile
# If they choose to select a profile, pass their name into the mainMenu function
# If they choose not to, prompt them to enter a name and set the caughtPkmn list to a random pokemon in the total pokemon list

def currentPkmn():
    '''Prints all of the pokemon the user has and their values along with gives them an option to level them up'''
    pass
# Prints the caughtPkmn list in a way so that the user can see each of them along with their corresponding CP value
# Asks the user to enter the index of the pokemon they want to level up
# Call the levelUp function with their index to level them up
# If the levelUp returns true, reprint everything
# Else tell the user they dont have enough candy and print the main menu

def selectPkmn():
    '''Prints each pokemon and lets the user select one. calls the getInput function and returns the value'''
    pass
# Prints the caughtPkmn list in a way so that the user can see each of them, their level, CP, and total candy the user has
# Lets the user select one and returns the index of the pokemon that they select

def levelUp(index):
    '''takes in a pokemon and returns true if theyre able to level them up and then updates the file'''
    pass
# Get the users caughtPkmn dict with the key using the index passed into this function
# Depending on the current level of the index of the pokemon, level up the pokemon and return true
# call the update function
# if the user doesnt have enough candy return false

def catchPkmn():
    '''Prompt the user to fight a pokemon and adds candy to the users account of they win'''
    pass
# Displays current pokemon and waits for the user to pick one
# The pokemon they pick will do random damage between the CP values to the one they're fighting
# They do this three times, if they don’t do 100 damage in those three turns, they lose
# If they win, add that pokemon to the users caughtPkmn list
# Add a random amount of candy to the inventory
# If not, don’t

def update():
    '''rewrites to the userfile to make sure that no progress is lost'''
    pass
# first it reads the file
# then for each line in the file, as long as the name of the file doesnt match userName, rewrite the file
# if it does match, dont rewrite and write the userName.totalCandy and then each pokemon in the caughtPkmn list

### MAIN ###
# Welcome and print instructions to the user
# userInput = user’s input
# While userInput not quit:
# print main menu
# If they select view current pokemon, print that to the screen via the currentPkmn() function
# If they select catch new pokemon, run catchPkmn() function
# run the update function
# Repeat until the user inputs quit
