from math import *
import numpy as np
import linecache
import matplotlib.pyplot as plt
#the inverse of reci_vector matrix
inv_b1x=float(2.0/sqrt(3))
inv_b1y=float(-1.0/sqrt(3))
inv_b1=[inv_b1x,inv_b1y,0]
inv_b2=[0,1,0]
reci_x=[0.293021605,0.169175630,0]
reci_y=[0.000000000,0.338351260,0]
def boundary(x,d):
    x_line=d*1.0/sqrt(3)
    midlv=x_line/2.0
    if x >-midlv and x < midlv:
        y=d
        return y
    elif x>=midlv:
        y=-sqrt(3)*x+2*d
        return y
    else:
        y=sqrt(3)*x+2*d
        return y
    pass
    
na=60;nb=60
d=0.5  #equal to the length of the Octagon
bmin=-d;bmax=d
amin=-d*2/sqrt(3);amax=d*2/sqrt(3)
cmin=cmax=0
na=int(nb*2.0/sqrt(3))
la=amax-amin;lb=bmax-bmin
da=float(la/na);db=float(lb/nb)
nn=0
for i in range(0,na+1):
    for j in range(0,nb+1):
        kx=amin+i*da
        ky=bmin+j*db
        if abs(ky) <= boundary(kx,d):
            nn=nn+1
print 'Number of kpoints:' +'    ' + str(nn)
tot_kp='     '+str(nn)
fname='./KPOINTS';f=open(fname,'w');f=file(fname,'a+')
f.writelines('Kmesh:'+'    '+str(na)+'    '+str(nb)+'    '+str(1))
f.write("\n")            
f.writelines(tot_kp)
f.write("\n")
f.writelines('Reciprocal lattice')
f.write("\n")
kz="%.15f" %(cmin)
for i in range(0,na+1):
    for j in range(0,nb+1):
        kx=amin+i*da
        ky=bmin+j*db
        if abs(kx)<da/2 and abs(ky)<db/2:
            ky="%.15f" %(0.0)
            kx="%.15f" %(0.0)
            plt.plot(kx,ky,'ro')
            linex='   '+str(kx)
            liney='   '+str(ky)
            line=liney+linex+'    '+str(kz)+'             '+str(1)
            f.writelines(line)
            f.write("\n")
            continue
        elif ky==0.0 and kx==0.0:
            kx="%.15f" %(0.0)
            ky="%.15f" %(0.0)
            plt.plot(kx,ky,'ro')
            linex='   '+str(kx)
            liney='   '+str(ky)
            line=liney+linex+'    '+str(kz)+'             '+str(1)
            f.writelines(line)
            f.write("\n")
            continue
        elif abs(ky) <= boundary(kx,d):
            dd=float(abs(ky)-boundary(kx,d))
            if dd<da*4/5.0 and dd>da/2:
                kkx="%.15f" %((amin+i*da)*inv_b1[0]+boundary(kx,d)*inv_b2[0])
                kky="%.15f" %((amin+i*da)*inv_b1[1]+boundary(kx,d)*inv_b2[1])
                linex='   '+str(kkx)
                liney='   '+str(kky)
                line=liney+linex+'    '+str(kz)+'             '+str(1)
                f.writelines(line)
                f.write("\n")
                kkkx=amin+i*da
                kkky=boundary(kx,d)
                plt.plot(kkkx,kkky,'ro')
            kx="%.15f" %((amin+i*da)*inv_b1[0]+(bmin+j*db)*inv_b2[0])
            ky="%.15f" %((amin+i*da)*inv_b1[1]+(bmin+j*db)*inv_b2[1])
            kxx="%.15f" %(((amin+i*da)*inv_b1[0]+(bmin+j*db)*inv_b2[0])*reci_x[0]+((amin+i*da)*inv_b1[1]+(bmin+j*db)*inv_b2[1])*reci_y[0])
            kyy="%.15f" %(((amin+i*da)*inv_b1[0]+(bmin+j*db)*inv_b2[0])*reci_x[1]+((amin+i*da)*inv_b1[1]+(bmin+j*db)*inv_b2[1])*reci_y[1])
            plt.plot(kxx,kyy,'ro')
            #plt.plot(ky,kx,'ro')
            linex='   '+str(kx)
            liney='   '+str(ky)
            line=liney+linex+'    '+str(kz)+'             '+str(1)
            f.writelines(line)
            f.write("\n")
plt.xlim(amin,amax)
plt.ylim(bmin,bmax)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
f.close()

