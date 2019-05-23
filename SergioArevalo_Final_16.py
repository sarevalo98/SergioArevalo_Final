import numpy as np
import random
def func(T0):
    D=1.593*T0
    return D
sigma=0.5
x = np.random.normal(0.0,sigma,10)
camino=[]
camino.append(x)

for i in range (100000):
	alpha = func(x+camino[-1])/func(camino[-1])
	
	if alpha>=1.0:
		camino.append(camino[-1]+x)
	else:
		beta = np.random.normal()
		
		if beta<=alpha:
			camino.append(camino[-1]+x)
		else:
			camino.append(camino[-1])
print(camino)
print("la velocidad del sonido en el mar es de 1.593 km/s.")