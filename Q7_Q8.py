import numpy as np
import matplotlib.pyplot as plt
File = open("Galaxy1.txt","r")
next(File)
x=[]
y=[]
p=100*10**6
for i in File.readlines():
    x.append(float(i.split()[0]))
    y.append(float(i.split()[1]))
x = np.array(x)
y = np.array(y)
x2 = np.arange(max(x))
y2 = x2*np.sqrt((4/3)*(4.3*10**-6)*(p)*np.pi)
plt.plot(x,y,"ro")
plt.plot(x2,y2)
plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (kms^-1)")
plt.axis([0,max(x),0,max(y)])
plt.show()
