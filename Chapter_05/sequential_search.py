def sequential_search(a_list, item):
	found = False
	pos = 0
	while pos < len(a_list) and not found:
		if a_list[pos] == item:
			found = True
		else:
			pos = pos +1
	return found
test_list = [1,2,3,4,5,6,7,8,9]
print(sequential_search(test_list, 1))
print(sequential_search(test_list, 0))
