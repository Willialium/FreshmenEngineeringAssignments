import matplotlib.pyplot as plt
import numpy as np

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        William Taylor
#               David Tanase
#               Henry Reinhardt
#               Timothy Bui
# Section:      209
# Assignment:   Lab 8-1
# Date:         18 10 2021
#

t = [0, 0.45, 1.1, 1.75, 2.25, 2.7]
y = [0, 0.23, 0.4, 0.18, 0.07, 0.01]

plot1maxX = 3.0
plot2maxX = 2.0

plot1X = np.arange(0, plot1maxX, .01)
plot2X = np.arange(0, plot2maxX, .01)
func1 = (plot1X ** 2) * np.exp(-1 * plot1X ** 2)
func2 = (plot1X ** 4) * np.exp(-1 * plot1X ** 2)


def function1(xVal):
    result = (xVal ** 2) * np.exp(-1 * xVal ** 2)
    return result


plt.figure('My Awesome ENGR 102 Plots.', edgecolor='m')
plt.subplot(2, 1, 1)
plt.plot(t, y, 'ko', label='data')
plt.plot(plot1X, func1, 'r', label='t^2exp(-t^2)')
plt.plot(plot1X, func2, 'b', label='t^4exp(-t^2)')
plt.legend(loc='upper right', frameon=True)
plt.xlim([0, 2.9])
plt.ylim([0, 1])
plt.xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5])
plt.xlabel('time')
plt.ylabel('y')
plt.title("Data and two curves vs. time")

plt.subplot(2, 1, 2)
plt.plot(t, y, 'y^', label='data')
plt.plot(t, y, 'y')
plt.plot(plot1X, func1, 'b', label='t^2exp(-t^2)')
plt.legend(loc='upper right')
plt.xlim([1, 2])
plt.ylim([0, .5])
plt.xlabel('time')
plt.ylabel('y')
plt.title("Data interpolation and Curve 1")
plt.annotate("It's closest here!", xy=(1.4, function1(1.4)), xytext=(1.2875, .15), fontsize=8,
             arrowprops=dict(arrowstyle='->'))

plt.tight_layout()
plt.show()
