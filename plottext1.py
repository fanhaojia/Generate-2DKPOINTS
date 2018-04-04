from math import *
import numpy as np
import matplotlib.pyplot as plt

def boundary(x,lv):
    hight=lv*sin(pi/3)
    midlv=lv/2
    if x >-midlv and x <midlv:
        y=hight
    elif x>0:
        k=-sqrt(3)
        y=k*x-k*lv
    elif x<0:
        k=sqrt(3)
        y=k*x+k*lv
    return y
    pass
na=30;nb=30   
lv=0.01  #lv equal to the length of the Octagon
amin=-lv;amax=lv
bmin=-lv;bmax=lv
cmin=cmax=0
la=amax-amin;lb=bmax-bmin
da=float(la)/na;db=float(lb)/nb
kxx=[0]*(na+1);kyy=[0]*(nb+1)
for i in range(0,na+1):
    for j in range(0,nb+1):
        kx=amin+i*da
        ky=bmin+j*db
        absky=abs(ky)
        if abs(kx)<da/2 and absky<db/2:
            kx="%.15f" %(0.0)
            ky="%.15f" %(0.0)
            plt.plot(kx,ky,'ro')
            kz="%.15f" %(cmin)
            linex='   '+str(kx)
            liney='   '+str(ky)
            line=linex+liney+'    '+str(kz)+'             '+str(1)
            continue
        elif kx==0.0 and ky==0.0:
            kx="%.15f" %(0.0)
            ky="%.15f" %(0.0)
            plt.plot(kx,ky,'ro')
            kz="%.15f" %(cmin)
            linex='   '+str(kx)
            liney='   '+str(ky)
            line=linex+liney+'    '+str(kz)+'             '+str(1)
            continue
        elif absky <boundary(kx,lv) or absky == boundary(kx,lv):
            kx="%.15f" %(amin+i*da)
            ky="%.15f" %(bmin+j*db)
            plt.plot(kx,ky,'ro')
            kz="%.15f" %(cmin)
            linex='   '+str(kx)
            liney='   '+str(ky)
            line=linex+liney+'    '+str(kz)+'             '+str(1)


plt.xlim(xmax=lv,xmin=-lv)
plt.ylim(ymax=lv,ymin=-lv)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
