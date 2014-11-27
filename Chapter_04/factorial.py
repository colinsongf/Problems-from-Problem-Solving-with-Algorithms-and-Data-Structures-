def factorial_n(n):
	if (n == 0 or n == 1):
		return 1
	else:
		return n*factorial_n(n-1)
print factorial_n(3)
