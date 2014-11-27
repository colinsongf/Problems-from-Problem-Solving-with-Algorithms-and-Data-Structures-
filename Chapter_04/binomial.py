def fact(n):
	if (n == 0 or n == 1):
		return 1
	else:
		return n * fact(n - 1)

def binomial(n,porc,r):
	if (porc == "c"):
		return (fact(n)/(fact(n-r) * fact(r)))
	elif(porc == "p"):
		return (fact(n) / fact(n-r))
	else:
		return "Not permutation & Combination"
print binomial(5,"p",2)
print binomial(5, "c", 2)
print binomial(5,"d", 2)


