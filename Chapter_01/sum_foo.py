import time
def foo(tom):
        start = time.time()
	fred = 0
	for bill in range(1, tom+1):
		barney = bill
		fred = fred + barney
        end = time.time()
	return fred, end-start
print(foo(10))
