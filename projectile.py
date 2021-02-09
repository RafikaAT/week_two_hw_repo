from math import pi
from math import tan
from math import cos
# This could also be written in one line to be made more efficient
print(pi)

y0 = 1
x = 0.5
v0 = 44
g = 9.81
theta = 80 * (pi/180)

y = y0 + (x*tan(theta)) - ((g*x**2)/(2*(v0*cos(theta))**2))
print(y)
