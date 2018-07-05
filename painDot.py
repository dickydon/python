import matplotlib.pyplot as plt
import numpy as np
import math
y = np.array([[1433,2500],[1671,2117]])
xDis = y[0,0] - y[1,0]
yDis = y[0,1] - y[1,1]
dis = xDis * xDis + yDis * yDis
print(xDis, yDis, dis, math.sqrt(dis))
d = 100
r = d / (math.sqrt(dis) - d)
x =(y[1,0] + r * y[0,0])/ (1 + r)
z = (y[1,1] + r * y[0,1])/(1 + r)
print(x,z)
a = y[1,0]-x 
b = y[1,1] - z 
print(a, b , math.sqrt( a * a  + b * b ))
a = np.array([[x,z]])
y = np.concatenate( (y, a))
plt.figure(figsize=(200,1)) 
plt.plot(y[:,0], y[0:,1], 'ro')
plt.grid(True)
plt.show()
