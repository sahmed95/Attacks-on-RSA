#Implementation of Blinding attack

import Cryptomath, random
from fractions import Fraction

def blind(M, public):
	#Returns a blinded message and the random r used to blind the message
	N = public[0]
	e = public[1]
	foundr = False
	while not foundr:
		r = random.randint(2, N-1)
		if Cryptomath.gcd(r, N) == 1:
			foundr = True
	m = (pow(r,e)*M)%N 
	print("r:", r)
	print("m:", m)
	    
def signature(s,r, public):
	N = public[0]
	for i in range(1000):
		m = s + i*N
		S = Fraction(m/r)
		if S.denominator == 1:
			break
	S = S%N
	print("S:",S)      
    



blind(2, [15,3])
