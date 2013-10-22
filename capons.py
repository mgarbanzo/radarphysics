#!/usr/bin/python

import numpy as np
from scipy import fftpack, pi
import matplotlib.pyplot as plt
from lags import *

N=64
m=16
Ts=1
freqs = -0.2, 0.2, -0.3, 0.3, 0.09

sgn = GenerateSignal(Ts, N, freqs)

#add some noise:
sgn = sgn + 1*np.random.rand(len(sgn))+ 1j*np.random.rand(len(sgn))
sgn = sgn-np.mean(sgn)
ary = ZeroPad(sgn,m-1)
Ry = np.cov(ary)
Ry = np.matrix(Ry)
RyI = Ry.I
print "RyI Shape: ", RyI.shape

#Defining the a(omega) vector:
omega = -2*pi/10
print "Omega: ", omega
m=np.arange(m)
a = np.exp(-m*omega*1j)

a=np.matrix(a)
print "a Shape: ", a.shape
print "a.H Shape: ", a.H.shape

#FILTER
h = RyI*a.T/(a.H.T*RyI*a.T)

HO = h.H*a.T
print HO, "This needs to be one"

w = np.arange(-pi,pi,0.01)     #Frequencies for the final freq response and freq content
H = np.zeros_like(w)           #H contains the freq response
P = np.zeros_like(w)           #P contains the freq content

for i,omega in enumerate(w):
	a = np.exp(-m*omega*1j)
	a=np.matrix(a)
	
	tmp1 = np.conjugate(h).T*a.T
	#Frequency response
	H[i] = np.real(np.abs(tmp1))
	#Power Spectral Density
	tmp2 = 1/(a.H.T*RyI*a.T)
	P[i] = np.real(np.abs(tmp2))
	
H=np.array(H)
P=np.array(P)

ft = fftpack.fft(sgn,n=10*len(sgn))
xv = np.fft.fftfreq(10*len(sgn),d=1)

plt.subplot(311)
plt.plot(w/(2*pi),np.real(H),'r-')
plt.plot(w/(2*pi),np.imag(H),'b-')
plt.subplot(312)
plt.plot(w/(2*pi),P,'ro')
plt.subplot(313)
plt.plot(xv,np.abs(ft),'ro')
plt.show()
