def ordered_sequential_search(a_list,item):
	pos = 0
	found =  False
	stop = False
	while pos < len(a_list) and not found and not stop:
		if a_list[pos] == item:
			found = True
		elif a_list[pos] > item:
			stop = True
		else:
			pos = pos+1
	return found
print (ordered_sequential_search([1,2,3,4,5],10)) 
