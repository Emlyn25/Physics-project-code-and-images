import math
import numpy as np
import matplotlib.pyplot as plt
File = open("Galaxy1.txt","r")
next(File)
radius=[]
V=[]
mV=[]
m=[]
DMmassV=[]
CmassV=[]
Cmass=[]
CmassP=[]
x2_P=[]
x2_S=[]
yerr=[]
all_p={}
finV=[]
#m[radius.index(i)]+ 4*math.pi*(100*10**6)*(1.87**2)*(i-1.87*np.arctan(i/1.87))




for i in File.readlines():
    radius.append(float(i.split()[0]))
    V.append(float(i.split()[1]))
    m.append(float(i.split()[4]))
for count in range(len(radius)):
    yerr.append(0.05)
for i in radius:
    DMmassV.append(math.sqrt((4.3*10**-6)*4*math.pi*(100*10**6)*(1.87**2)*(i-1.87*np.arctan(i/1.87))*1/i))
for i in radius:  
    CmassV.append(math.sqrt((4.3*10**-6)*(m[radius.index(i)]+4*math.pi*(100*10**6)*(1.87**2)*(i-1.87*np.arctan(i/1.87)))*1/i))
for i in radius:
    mV.append(math.sqrt((4.3*10**-6)*m[radius.index(i)]*1/i))
for i in radius:  
    Cmass.append(((m[radius.index(i)]+4*math.pi*(100*10**6)*(1.87**2)*(i-1.87*np.arctan(i/1.87))))/(4*math.pi*1.87**2)*(i-1.87*np.arctan(i/1.87)))
    

    """for i in y:
        x2.append(((i-(fx[y.index(i)])*slope.item())**2)*( 1/(yerr[y.index(i)])**2))"""
    """(math.sqrt((4.3*10**-6)*(m[radius.index(o)]+4*math.pi*(i)*(1.87**2)*(o-1.87*np.arctan(o/1.87)))*1/o))"""

for i in Cmass:
    CmassP=[]
    for o in radius:
        CmassP.append(math.sqrt((4.3*10**-6)*4*math.pi*(i)*(1.87**2)*(o-1.87*np.arctan(o/1.87))*1/o))
    all_p.update({i:CmassP})
#print(all_p.keys())
count=0
for i in all_p:
    count=0
    x2=[]
    for o in all_p[i]:
        x2.append(((o-(radius[count]))**2)/(yerr[count])**2)
        count+=1
    x2_S.append(np.sum(x2))
    x2_P.append(i)

#x2_P[x2_S.index(min(x2_S))]
for i in radius:
    finV.append(math.sqrt((4.3*10**-6)*(m[radius.index(i)]+4*math.pi*(x2_P[x2_S.index(min(x2_S))])*(1.87**2)*(i-1.87*np.arctan(i/1.87)))*1/i))


mV=np.array(mV)
radius = np.array(radius)
y = np.array(DMmassV)
CmassV = np.array(CmassV)
finV=np.array(finV)
#fx2=minslope*radius

plt.plot(radius,finV)
plt.plot(radius,CmassV)#combined DM and Visable mass
plt.plot(radius,mV)#prediction based on mass from data
plt.plot(radius,y)#DM
plt.plot(radius,V)#actual data
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (kms^-1)")
plt.axis([0,max(radius),0,max(V)+2])
plt.show()
