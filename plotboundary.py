from math import *
import numpy as np
import linecache
import matplotlib.pyplot as plt

def boundary(x,d):
    hight=d*sin(pi/3)
    midlv=d/2.0
    if x >-midlv and x < midlv:
        y=hight
        return y
    elif x>midlv:
        k=-sqrt(3)
        y=k*x-k*d
        return y
    else:
        k=sqrt(3)
        y=k*x+k*d
        return y
    pass

d=2.0
for i in range(0,400):
    x=-d+0.01*i
    y=boundary(x,d)
    plt.plot(x,y,'ro')

plt.xlim(xmax=d,xmin=-d)
plt.ylim(ymax=d,ymin=-d)
plt.xlabel("x")
plt.ylabel("y")
plt.show()



