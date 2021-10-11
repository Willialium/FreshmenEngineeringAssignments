from sympy import *
from sympy.plotting import (plot, plot_parametric)


d = symbols("d")

M = .1
pw = 1000.0
C = 1.0
theta = 10*pi/180
B = 10*pi/180
g = 9.81

vNumerator = sqrt((16*M*g)/(pi*C*pw*d**2))
vDenominator = sqrt(1 - (8 * M * tan(B)**2)/(pi * (d**3)*C*pw*sin(theta)))

vod = vNumerator/vDenominator

#plot(vod, (d, .05, .1), ylim=(.7, .9))
print(solve(vod-.8,d))