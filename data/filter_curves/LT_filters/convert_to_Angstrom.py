import numpy as np

for flt in ['u','g','r','i','z']:
	curvefile = 'LT_IOO_{}.txt'.format(flt)
	curvefilenew = 'LT_IOO_{}_lambdaA.txt'.format(flt)

	data = np.loadtxt(curvefile, skiprows=1)
	data[:,0] = data[:,0]*10

	np.savetxt(curvefilenew, data)
