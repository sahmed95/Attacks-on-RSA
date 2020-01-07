
def gcd(a, b):
    # Returns the GCD of positive integers a and b using the Euclidean Algorithm.
    x, y = a, b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

def extendedGCD(a,b):
    # Returns integers u, v such that au + bv = gcd(a,b).
    x, y = a, b
    u1, v1 = 1, 0
    u2, v2 = 0, 1
    while y != 0:
        r = x % y
        q = (x - r) // y
        u, v = u1 - q*u2, v1 - q*v2
        x = y
        y = r
        u1, v1 = u2, v2
        u2, v2 = u, v
    return (u1, v1)

def findModInverse(a, m):
    # Returns the inverse of a modulo m, if it exists.
    if gcd(a,m) != 1:
        return None
    u, v = extendedGCD(a,m)
    return u % m
    

def encryption(m, public): 
	#Converts plaintext to ciphertext
	exp = public[1]
	N = public[0]
	c = pow(m, exp)% N
	return c
	
def decryption(c, private):
	#Converts ciphertext to plaintext
	exp = private[1]
	N = private [0]
	m = pow(c, exp)%N
	return m
	
