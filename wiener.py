#Implementation of M. Wiener's Low Private Exponent Attack

import Cryptomath, math
from fractions import Fraction

def euclid(a,b): 
    # Returns the GCD of positive integers a and b using the Euclidean Algorithm.
	x, y = int(a), int(b)
	list = []
	while y != 0:
		list.append(x//y)
		r = x % y
		x = y
		y = r
	return list

	


def wiener(public):
	N = int(public[0])
	e = int(public[1])
	a = euclid(e,N)
	print('expansion:', a)
	n0 = a[0]
	d0 = 1
	n1 = a[0]*a[1] + 1
	d1 = a[1]
	list = [Fraction(n0,d0),Fraction(n1,d1)]

	for x in a[2:]:
		n = x*n1 + n0 # numerator
		d = x*d1 + d0 # denominator
		list.append(Fraction(n,d))
		n1, n0 = n, n1
		d1, d0 = d, d1

	for l in list: 
		if l.numerator != 0:
			M = ((e*l.denominator) -1)/l.numerator
			b = (N + 1 - M)*(-1)
			c = N
			r = pow(b,2) - 4*c
			p = 0
			q = 0
			if r > 0:
				p = ((((-b) - math.sqrt(r))/(2)))
				q = (((-b) + math.sqrt(r))/(2))
		
				if (p * q) == N: 
					phi = M
					d = Cryptomath.findModInverse(e,phi)
					if d!= None:
						break
	print('p:', p)
	print('q:', q)
	print('d:', d)

