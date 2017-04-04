import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

pop=[3.0, 4.0, 4.9, 5.7, 14.8, 24.7, 26.2, 38.3, 63.8, 65.7, 69.6]
cal=[3642, 3432, 3049, 3273, 3394, 2687, 2643, 2192, 2204, 2159, 2628]

num=0
den=0
den2=0
for i in range(0,10):
    num+=( pop[i]-np.mean(pop) ) * ( cal[i]-np.mean(cal))
    den+= (pop[i]-np.mean(pop))**2
    den2+= (cal[i]-np.mean(cal))**2
    
B1=num/den
r=num/(sqrt(den)*sqrt(den2))
B0=np.mean(cal) - B1* np.mean(pop)

print(B1)
print(B0)
print(r)
x=np.linspace(0,80);
reglin=B1*x+B0

plt.plot(pop,cal,'o')
plt.plot(x,reglin)                                    
plt.show()

