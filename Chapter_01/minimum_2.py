def min(a):
	m=a[0]
	for i in a[1:]:
		if m>i:
			m=i
	print m
min([1,4,2,6,1,0])
