import numpy as np
import matplotlib.pyplot as plt
x=[5,10,15,20,25]
y=[0.2,0.5,0.8,1.0,1.3]
yerr = [0.05,0.05,0.05,0.05,0.05]
fx=[]
#fx=0.04*x
for i in x:
    fx.append(0.04*i)
x2=[]
"""for i in y:
    x2.append(((i-fx[y.index(i)])**2)*( 1/(yerr[y.index(i)])))"""
x= np.array(x)
start=0
stop=1
step=0.001
minchi2=10000
minslope=0.0
for slope in np.arange(start, stop, step):
    """for i in y:
        x2.append(((i-(fx[y.index(i)])*slope.item())**2)*( 1/(yerr[y.index(i)])**2))"""
    count=0
    for i in x:
        x2.append(((y[count]-(i*slope))**2)/(yerr[count])**2)
        count+=1

        
    chi2 =np.sum(x2)
    x2=[]
    if(chi2<minchi2):
        minchi2=chi2
        minslope=slope


y= np.array(y)
fx= np.array(fx)

fx2=minslope*x
fxn=0.05*x
yerr= np.array(yerr)
plt.errorbar(x,y,yerr,fmt="bo")
plt.plot(x,fx,"b-")
plt.plot(x,fxn,"y-")
plt.plot(x,fx2,"g-")
plt.plot()
plt.show()
