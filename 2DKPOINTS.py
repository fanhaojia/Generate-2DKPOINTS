from math import *
import numpy as np
import linecache
import matplotlib.pyplot as plt
na=19
nb=19 #(na+1)*(nb+1) = k points denstiy
amin=-0.1
amax=0.1
bmin=-0.1
bmax=0.1
cmin=cmax=0
la=amax-amin
lb=bmax-bmin
da=float(la)/na
db=float(lb)/nb
a=[0]*na;b=[0]*nb
nab=(na+1)*(nb+1)
tot_kp='     '+str(nab)
fname='./KPOINTS'
f=open(fname,'w')
f=file(fname,'a+')
f.writelines('Automatically generated mesh')
f.write("\n")
f.writelines(tot_kp)
f.write("\n")
f.writelines('Reciprocal lattice')
f.write("\n")

for i in range(0,na+1):
    for j in range(0,nb+1):
        kx="%.15f" %(amin+i*da)
        ky="%.15f" %(bmin+j*db)
        x=amin+i*da
        y=bmin+j*db
        kxx="%.15f" %(x*0.5*sqrt(3))
        kyy="%.15f" %(x*0.5+y)
        plt.plot(kxx,kyy,'ro')
        kz="%.15f" %(cmin)
        #if (amin+i*da)<amax:
        #    linex='   '+str(kx)
        #else:
        #    linex='    '+str(kx)
        #if (bmin+j*db)<bmax:
        #    liney='   '+str(ky)
        #else:
        #    liney='    '+str(ky)
        linex='   '+str(kx)
        liney='    '+str(ky)
        line=linex+liney+'    '+str(kz)+'             '+str(1)
        f.writelines(line)
        f.write("\n")
plt.xlim(xmax=-0.2,xmin=0.2)
plt.ylim(ymax=-0.2,ymin=0.2)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
f.close()
