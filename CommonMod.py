#Implemention of Common Modulus Attack

import Cryptomath, random

def Ntod(p,q, public):
 
 	N = public[0]
 	e = public[1]
 	phi = (p-1)*(q-1) 
 	d = Cryptomath.findModInverse(e, phi)
 	return d


def dtoN(d, public):
	N = public[0]
	e = public[1]
	k = d*e - 1
		
	g = random.randint(2, N)
	t = k 
	x = 0 
	gcd = 0
	foundfactor = False
	while not foundfactor:
		t = t/2
		x = (pow(g,t))%N
		gcd = Cryptomath.gcd(x-1, N)
		if x > 1 and gcd >1: 
			foundfactor = True
	p = int(gcd)
	q = int(N/gcd)		
		
	return [p,q]


def commonmod(public, private, public_a, C):
	N = public[0]
	e = public[1]
	d = private[1]
	e_a = public_a[1]
	factors = dtoN(d, [N,e])
	p = int(factors[0])
	q = int(factors[1])
	print("p:", p, "q:",q)
	d_a = Ntod(p,q, public_a)
	print("d:", d_a)
	M = pow(C, d_a) % N
	print("M:", M)		

commonmod([21, 11], [21,11],[21, 5], 4)