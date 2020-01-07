#Implementation of Broadcast attack
# For simplicity's sake, we will assume all public exponents are equal to 3. 

import Cryptomath,math

def hastad(e=3, public1 = [], public2= [], public3=[], c1 =0, c2=0, c3 = 0):
	N1 = public1[0]
	N2 = public2[0]
	N3 = public3[0]
	N = N1*N2*N3
	n1 = N/N1
	n2 = N/N2
	n3 = N/N3
	d1 = Cryptomath.findModInverse(n1, N1)
	d2 = Cryptomath.findModInverse(n2, N2)
	d3 = Cryptomath.findModInverse(n3, N3)
	C = (c1*d1*n1 + c2*d2*n2 + c3*d3*n3)%N   
	M = int(round(pow(C,1/3)))
	print("Message:",M)

