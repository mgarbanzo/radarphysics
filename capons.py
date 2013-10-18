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
a = np.zeros_like(range(m))+np.zeros_like(range(m),complex)

omega = -0.1
print "Omega: ", omega
for m in range(len(a)):
    a[m] = np.complex(np.cos(-m*omega),np.sin(-m*omega))

a=np.matrix(a)
print "a Shape: ", a.shape
print "a.H Shape: ", a.H.shape

h = RyI*a.T/(a.H.T*RyI*a.T)

print h

HO = h.H*a.T
print HO

w = np.arange(-pi,pi,0.01)
H = np.zeros_like(w)

#Frequency response
for i,k in enumerate(w):
	a = np.zeros_like(range(16))+np.zeros_like(range(16),complex)
	for m in range(len(a)):
		a[m] = np.complex(np.cos(-m*k),np.sin(-m*k))
	a=np.matrix(a)
	tmp = np.conjugate(h).T*a.T
	#print tmp
	H[i] = np.real(np.abs(tmp))

H=np.array(H)
#Power Spectral Density

P = np.zeros_like(w)

for i,k in enumerate(w):
	a = np.zeros_like(range(16))+np.zeros_like(range(16),complex)
	for m in range(len(a)):
		a[m] = np.complex(np.cos(-m*k),np.sin(-m*k))
	a=np.matrix(a)
	tmp = 1/(a.H.T*RyI*a.T)
	#print tmp
	P[i] = np.real(np.abs(tmp))

P=np.array(P)

ft = fftpack.fft(sgn,n=len(sgn))
xv = np.fft.fftfreq(len(sgn),d=1)

plt.subplot(311)
plt.plot(np.real(sgn))
plt.plot(np.imag(sgn))
plt.subplot(312)
plt.plot(w,P)
plt.subplot(313)
plt.plot(xv,np.abs(ft))
plt.show()
