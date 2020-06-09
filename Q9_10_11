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

#m[radius.index(i)]+ 4*math.pi*(100*10**6)*(1.87**2)*(i-1.87*np.arctan(i/1.87))




for i in File.readlines():
    radius.append(float(i.split()[0]))
    V.append(float(i.split()[1]))
    m.append(float(i.split()[4]))

for i in radius:
    DMmassV.append(math.sqrt((4.3*10**-6)*4*math.pi*(100*10**6)*(1.87**2)*(i-1.87*np.arctan(i/1.87))*1/i))
for i in radius:  
    CmassV.append(math.sqrt((4.3*10**-6)*(m[radius.index(i)]+4*math.pi*(100*10**6)*(1.87**2)*(i-1.87*np.arctan(i/1.87)))*1/i))
for i in radius:
    mV.append(math.sqrt((4.3*10**-6)*m[radius.index(i)]*1/i))



mV=np.array(mV)
radius = np.array(radius)
y = np.array(DMmassV)
CmassV = np.array(CmassV)
plt.plot(radius,CmassV)#combined DM and Visable mass
plt.plot(radius,mV)#prediction based on mass from data
plt.plot(radius,y)#DM
plt.plot(radius,V)#actual data
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (kms^-1)")
plt.axis([0,max(radius),0,max(V)+2])
plt.show()
