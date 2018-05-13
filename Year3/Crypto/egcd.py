def egcd(a, b):
	'''result[2] is the modulo inverse of b mod a. only when result[0] is 1'''
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)
