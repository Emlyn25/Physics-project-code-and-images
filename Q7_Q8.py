import math
import numpy as np
import matplotlib.pyplot as plt
File = open("Galaxy1.txt","r")
next(File)
x=[]
y=[]
m=[]
for i in File.readlines():
    x.append(float(i.split()[0]))
    y.append(float(i.split()[1]))
    m.append(float(i.split()[4]))
x = np.array(x)
y = np.array(y)

y2=[]
x2 = list(range(1, int(max(x))))
for i in x2:
    if i==0: next
    else:

        y2.append(math.sqrt((4.3*10**-6) * m[x2.index(i)] * 1/i))

x2=np.array(x2)
        
y2 = np.array(y2)
plt.plot(x,y)
plt.plot(x2,y2)
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (kms^-1)")
plt.axis([0,max(x),0,max(y)+2])
plt.show()
