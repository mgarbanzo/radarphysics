import numpy as np
import matplotlib.pyplot as plt

def ZeroPad(y, m):
	"""This function is very important, it actually prepares the signal
	to be used in the covariance function. The way this works is adding 
	zeros at the beginning or end of a data array. In this manner the
	zero lag will be just the NO ZERO ADDED to the begining OR (this is
	hard to see at first) any index reapeted in both functions for the
	covariance, meaning that the result of y[n] y*[n] = y[n-1] y*[n-1].
	These values create the diagonal as equal values even when it does
	not seems correct."""
	
	vector = []
	
	for lag in range(m+1):
		temp = y.copy()
		for j in range(lag):
			temp=np.append(0,temp)
		for i in range(m-lag):
			temp=np.append(temp,0)
		vector.append(temp)
	return vector

def GenerateSignal(Ts, N, freqs):
	"""This function takes the separation in time to be used (Ts) to 
	create a time vector of N entries.
	The freqs array constains the frequencies used to create the complex
	signal that is generated"""
	
	time = np.arange(0,N,1)
	sgn = np.zeros_like(time)+np.zeros_like(time,complex)
	for freq in freqs:
		real = np.cos(2*np.pi*freq*time)
		imag = np.sin(2*np.pi*freq*time)
		for n in range(len(time)):
			sgn[n] += np.complex(real[n],imag[n])
	return sgn

#N=64
#m=16
#Ts=1
#freqs = -0.2, 0.2, -0.3, 0.3, 0.09

#sgn = GenerateSignal(Ts, N, freqs)
#ary = ZeroPad(sgn,m)

#plt.plot(np.real(sgn))
#plt.plot(np.imag(sgn))
#print ary
#print np.cov(ary)
#plt.show()
