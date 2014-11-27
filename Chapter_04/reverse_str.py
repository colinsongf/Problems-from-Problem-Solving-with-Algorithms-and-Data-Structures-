def reverse_str(my_str):
	if len(my_str) == 1:
		return my_str[-1]
	else:
		return my_str[-1] + reverse_str(my_str[:-1])
print (reverse_str("abcdefghijklm"))
