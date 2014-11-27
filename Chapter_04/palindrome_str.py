def palindrome_str(my_str):
	if len(my_str) == 1:
		print "The given string is a palindrome"
	else:
		if my_str[0] == my_str[-1]:
			palindrome_str(my_str[1:-1])
		else:
			print "The given string is not a palindrome"
print (palindrome_str("malayalam"))
print (palindrome_str("english"))
