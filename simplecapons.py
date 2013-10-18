#!/usr/bin/python

import numpy as np
from scipy import fftpack, pi
import matplotlib.pyplot as plt

#Frequencies to be used in the signal
freqs = 0.09, -0.2, 0.2, -0.3, 0.3

time = np.arange(0,64,1)
sgn = np.zeros_like(time)+np.zeros_like(time,complex)

sgn1 = np.zeros_like(time)+np.zeros_like(time,complex)
sgn2 = np.zeros_like(time)+np.zeros_like(time,complex)
sgn3 = np.zeros_like(time)+np.zeros_like(time,complex)
sgn4 = np.zeros_like(time)+np.zeros_like(time,complex)
sgn5 = np.zeros_like(time)+np.zeros_like(time,complex)

M=np.mat([sgn1,sgn2,sgn3,sgn4,sgn5])

k=0
for freq in freqs:
	real = np.cos(2*pi*freq*time)
	imag = np.sin(2*pi*freq*time)
	for n in range(len(time)):
		sgn[n] = np.complex(real[n],imag[n])
	M[k] = sgn
	k+=1
	
np.set_printoptions(precision=5,suppress=True)
Ry = M*M.H
print Ry
RyI = Ry.I
print RyI
print "RyI Shape: ", RyI.shape

##Defining the a(omega) vector:
a = np.zeros_like(range(5))+np.zeros_like(range(5),complex)

omega = -0.1
print "Omega: ", omega
for m in range(len(a)):
    a[m] = np.complex(np.cos(-m*omega),np.sin(-m*omega))

a=np.matrix(a)
print a
print "a Shape: ", a.shape
print "a.H Shape: ", a.H.shape

h = RyI*a.T/(a.H.T*RyI*a.T)

print "h",h

HO = np.conjugate(h).T*a.T
print "At the value of w is should be 1: ",HO,np.abs(HO)

w = np.arange(-pi,pi,0.01)
H = np.zeros_like(w)

for i,k in enumerate(w):
	a = np.zeros_like(range(5))+np.zeros_like(range(5),complex)
	for m in range(len(a)):
		a[m] = np.complex(np.cos(-m*k),np.sin(-m*k))
	a=np.matrix(a)
	tmp = np.conjugate(h).T*a.T
	#print tmp
	H[i] = np.real(np.abs(tmp))
	
#print H
H=np.array(H)

P = np.zeros_like(w)

for i,k in enumerate(w):
	a = np.zeros_like(range(5))+np.zeros_like(range(5),complex)
	for m in range(len(a)):
		a[m] = np.complex(np.cos(-m*k),np.sin(-m*k))
	a=np.matrix(a)
	tmp = 1/(a.H.T*RyI*a.T)
	#print tmp
	P[i] = np.real(np.abs(tmp))

P=np.array(P)

plt.plot(w,P)
plt.show()
#~ plt.plot(xv,np.real(ft))
#~ plt.plot(xv,np.imag(ft))
#~ plt.show()
