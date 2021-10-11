from numpy import *
import matplotlib.pyplot as plt

velocity = float(input("Enter velocity: "))
xDistance = 202.4
gravity = 9.8


def height(theta):
    theta *= (pi / 180)
    height = (xDistance * tan(theta)) - ((gravity * xDistance ** 2) / (2 * velocity ** 2 * (cos(theta) ** 2)))
    if (height == 0):
        return -1
    return height


angle = 0.0
while (height(angle) < .9 and height(angle + .1) > height(angle)):
    angle += .1

if (height(angle) < .9):
    print("If the bird is shot at a velocity of {} m/s,\n"
        "it will never reach a height of 1m (+- .1m)".format(velocity))

else:
    print("If the bird is shot at an angle of {:.2f} degrees at a velocity of {} m/s,\n"
          "it will reach a height of {:.2f}m".format(angle, velocity, height(angle)))

    lower_range_val = 0
    upper_range_val = xDistance
    xvals = arange(lower_range_val, upper_range_val, .1)
    angle *= (pi / 180)
    yvals = (xvals * tan(angle)) - ((gravity * xvals ** 2) / (2 * velocity ** 2 * (cos(angle) ** 2)))
    # Create and show plot
    plt.plot(xvals, yvals)  # Creates line plot with yvals (vertical axis) plotted against xvals (horizontal axis)
    plt.show()

print("If on mars: ")

gravity = 3.71

angle = 0.0
while (height(angle) < .9 and height(angle + .1) > height(angle)):
    angle += .1

if (height(angle) < .9):
    print("If the bird is shot at a velocity of {} m/s,\n"
        "it will never reach a height of 1m (+- .1m)".format(velocity))

else:
    print("If the bird is shot at an angle of {:.2f} degrees at a velocity of {} m/s,\n"
        "it will reach a height of {:.2f}m".format(angle, velocity, height(angle)))

    lower_range_val = 0
    upper_range_val = xDistance
    xvals = arange(lower_range_val, upper_range_val, .1)
    angle *= (pi / 180)
    yvals = (xvals * tan(angle)) - ((gravity * xvals ** 2) / (2 * velocity ** 2 * (cos(angle) ** 2)))
    # Create and show plot
    plt.plot(xvals, yvals)  # Creates line plot with yvals (vertical axis) plotted against xvals (horizontal axis)
    plt.show()
