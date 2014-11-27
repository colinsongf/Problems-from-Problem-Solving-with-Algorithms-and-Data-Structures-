class Stack:
         def __init__(self):
                 self.items = []
         def is_empty(self):
                 return self.items == []
         def push(self, item):
                 self.items.append(item)
         def pop(self):
                 return self.items.pop()
         def peek(self):
                 return self.items[len(self.items) - 1]
         def size(self):
                 return len(self.items)
def divided_by_two(decimal_num):
	stack_rem = Stack() 
	while decimal_num > 0:
		rem = decimal_num % 2
                stack_rem.push(rem)
                decimal_num  // 2
	b = ""
        while not stack_rem.is_empty():
		b = b + str(stack_rem.pop())
	return b
print(divided_by_two(17))
print(divided_by_two(45))
print(divided_by_two(96))
 


