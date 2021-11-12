# Standard Header Here
# ----------------------------------------- IMPORT STATEMENTS------------------------------------------ # (Put the necessary import statements first)
from math import *
from numpy import *
import matplotlib.pyplot as plt


# ---------------------------------------- FUNCTION DEFINITIONS-----------------------------------------
# (Create and place any needed function definitions in this part of the program)
# If you see a function being used that doesn’t already have a definition in this area, you will # need to create it.


def trajectory_y(x, g, vo, angle):
    """Returns (y-value) of the trajectory for a given x-value, gravity, initial velocity, and angle."""
    angle = radians(angle)
    return (x * tan(angle)) - (g * x ** 2) / (2 * (vo ** 2) * cos(angle) ** 2)


# Gets the bird from the user, the returned value contains the name, color, and size of the bird
def bird_picker():
    birds = {'Red': ('Red', 'r', 2),
             'Chuck': ('Chuck', 'y', 2),
             'Bomb': ('Bomb', 'k', 7),
             'Terence': ('Terence', 'r', 7)}

    print('Please type the name of the bird you would like:')
    print('\tRed is a small, red bird')
    print('\tChuck is a small, yellow bird')
    print('\tBomb is a large, black bird')
    print('\tTerence is a large, red bird ')
    bird = input('Enter name -> ')

    return birds[bird]


# Gets the planet from the user, the returned value is a float containing the acceleration due to gravity
def planet_picker():
    planets = {'Earth': (9.807),
               'Mars': (3.711),
               'Moon': (1.625),
               'Jupiter': (24.79)}

    print('Please type the name of the planet you would like:')
    print("\tEarth with an acceleration of 9.807 m/s^2")
    print("\tMars with an acceleration of 3.711 m/s^2")
    print("\tMoon with an acceleration of 1.625 m/s^2")
    print("\tJupiter with an acceleration of 24.79 m/s^2")

    planet = input('Enter planet name -> ')

    return planets[planet]


# Gets the guesses for velocity and angle, the returned values are floats
def get_guesses():
    velGuess = float(input('Enter your guess at the initial velocity of the bird (number) -> '))
    angGuess = float(input('Enter your guess at the initial angle of the bird (number in degrees) -> '))

    return velGuess, angGuess


# Gets a list from 0 to 1000 (The max location for the pig) and the y list contains the corresponding y value of each x value
def trajectory(gravity, vGuess, thetaGuess):
    xList = arange(0, 1000, .1)
    yList = [trajectory_y(float(xVal), gravity, vGuess, thetaGuess) for xVal in xList.tolist()]

    return xList, yList


# Checks if any point on the line is within the bounds of the pig, taking in to account the size of the pig
def hit(x, y, target):
    # distance (x from 10-1000), height (y from 0-50) and size of a target

    for i in range(len(x)):
        xHits = False
        yHits = False
        if (target[0] - target[2] / 2) <= x[i] <= (target[0] + target[2] / 2):
            xHits = True

        if (target[1] - target[2] / 2) <= y[i] <= (target[1] + target[2] / 2):
            yHits = True

        if (xHits and yHits):
            return True

    return False


# Plots the graph

def birds_plot(x, y, target, bird, doesHit=False):
    print(bird)
    plt.title("{}'s trajectory".format(bird[0]))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, bird[1] + '--', linewidth=bird[2])
    plt.plot(target[0], target[1], "go")

    # If the bird was hit, put a red x on it
    if doesHit:
        plt.plot(target[0], target[1], "rx")
    plt.ylim(0, max(y) + 20)
    plt.xlim(0, target[0] + 20)
    plt.show()


def get_basics():
    """Takes user selections for active bird and planet. Returns (bird, planet). 'Bird' includes name, color and size. 'Planet' includes name and gravity. """
    a = bird_picker()  # Runs fn to provide bird menu
    b = planet_picker()  # Runs fn to provide planet menu
    return a, b


# -------------------------------------------- MAIN PROGRAM -------------------------------------------- # (The Main Program is below – you WILL NOT need to make any changes or additions to this part.)
# Sets up loop so user can repeat the game as many times as desired ('y' to continue, 'n' to quit)
pig_counter = 0
again = 'y'
while again == 'y':
    # Program will pick a random distance (x from 10-1000), height (y from 0-50) and size of a target
    target = (random.randint(10, 1000), random.randint(0, 50), random.randint(10, 50))

    # Obtains user selections and initial guesses
    bird, g = get_basics()  # Runs fn to get bird and planet (gravity) selection
    v_guess, theta_guess = get_guesses()  # Runs fn to get initial velocity and angle guesses

    # Loops guesses until bird hits target
    x, y = trajectory(g, v_guess, theta_guess)  # Runs fn to create current x- and y- value lists
    while not hit(x, y, target):  # Program cycles until thrown bird hits the target
        birds_plot(x, y, target, bird)  # Plots trajectory & target of miss
        print("Wrong, try again")
        v_guess, theta_guess = get_guesses()  # Gets updated guesses from user
        x, y = trajectory(g, v_guess, theta_guess)  # Creates updated lists of x- and y-values

    # Handles winning case and asks if user would like to play again
    print('Yay!')
    pig_counter += 1
    # Plots trajectory and target of a hit
    birds_plot(x, y, target, bird, True)
    again = input('Would you like to play again? (y/n)')
    while again not in {'y', 'n'}:
        again = input('Please type either y or n only. Would you like to play again? (y/n)')
# Exiting when user decides to quit
print('\nThanks for playing! you popped {} pig(s) today!'.format(pig_counter))
