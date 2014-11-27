def head(xs):
    return xs[0]

def tail(xs):
    return xs[1:]

def empty(xs):
    return len(xs) == 0

def reverse(xs):
	if empty(xs):
		return []
    
	else:
		return reverse(tail(xs))+[head(xs)]
print (reverse([1,2,3]))
