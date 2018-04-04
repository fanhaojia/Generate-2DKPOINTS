from math import *
import numpy as np
import linecache
import matplotlib.pyplot as plt
def boundary(x,lv):
    hight=lv*sin(pi/3)
    midlv=lv/2.0
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
lv=1.0  #lv equal to the length of the Octagon
amin=-lv;amax=lv
bmin=-lv;bmax=lv
cmin=cmax=0
la=amax-amin;lb=bmax-bmin
da=float(la)/na;db=float(lb)/nb
nn=0
for i in range(0,na+1):
    for j in range(0,nb+1):
        kx=amin+i*da
        ky=bmin+j*db
        absky=abs(ky)
        if absky <boundary(kx,lv) or absky == boundary(kx,lv):
            nn=nn+1
tot_kp='     '+str(nn)
fname='./KPOINTS';f=open(fname,'w');f=file(fname,'a+')
f.writelines('Automatically generated mesh')
f.write("\n")            
f.writelines(tot_kp)
f.write("\n")
f.writelines('Reciprocal lattice')
f.write("\n")
for i in range(0,na+1):
    for j in range(0,nb+1):
        kx=amin+i*da
        ky=bmin+j*db
        absky=abs(ky)
        if abs(kx)<da/2 and absky<db/2:
            kx="%.15f" %(0.0)
            ky="%.15f" %(0.0)
            kz="%.15f" %(cmin)
            plt.plot(kx,ky,'ro')
            linex='   '+str(kx)
            liney='   '+str(ky)
            line=linex+liney+'    '+str(kz)+'             '+str(1)
            f.writelines(line)
            f.write("\n")
            continue
        elif kx==0.0 and ky==0.0:
            kx="%.15f" %(0.0)
            ky="%.15f" %(0.0)
            kz="%.15f" %(cmin)
            plt.plot(kx,ky,'ro')
            linex='   '+str(kx)
            liney='   '+str(ky)
            line=linex+liney+'    '+str(kz)+'             '+str(1)
            f.writelines(line)
            f.write("\n")
            continue
        elif absky <boundary(kx,lv) or absky == boundary(kx,lv):
            kx="%.15f" %((amin+i*da)*2/sqrt(3))
            ky="%.15f" %(bmin+j*db-(amin+i*da)/sqrt(3))
            #kx="%.15f" %(amin+i*da)
            #ky="%.15f" %(bmin+j*db)
            x=(amin+i*da)*2/sqrt(3)
            y=bmin+j*db-(amin+i*da)/sqrt(3)
            #x=amin+i*da
            #y=bmin+j*db
            kxx="%.15f" %(x*0.5*sqrt(3))
            kyy="%.15f" %(x*0.5+y)
            plt.plot(kxx,kyy,'ro')
            kz="%.15f" %(cmin)
            linex='   '+str(kx)
            liney='   '+str(ky)
            line=linex+liney+'    '+str(kz)+'             '+str(1)
            f.writelines(line)
            f.write("\n")
plt.xlim(xmax=2*lv,xmin=-lv*2)
plt.ylim(ymax=2*lv,ymin=-lv*2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
f.close()
