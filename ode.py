import numpy as np
import matplotlib.pyplot as plt
from math import *

def change_to_rect(polar):
    return [[r*cos(angle),r*sin(angle)] for r,angle in polar]
def change_to_polar(rect):
    return [[sqrt(x**2 + y**2),atan(y/x)] for x,y in rect]
r0 = 1
g = 9.8
dt = 0.001
rf = 0.874
def fun_d2f(r):
    return 0.5*g/r**3 - 3*g
r = r0
dr = 0
radius =[]
while r>rf:
    r += dr*dt
    radius.append(r)
    dr += fun_d2f(r)*dt
angle = []
a = 0.0
for i in radius:
    angle.append(a)
    a += (sqrt(2*g)/i**2)*dt
data = zip(radius,angle)

x,y = zip(*change_to_rect(data))

plt.plot(x,y,"*")
plt.show()
