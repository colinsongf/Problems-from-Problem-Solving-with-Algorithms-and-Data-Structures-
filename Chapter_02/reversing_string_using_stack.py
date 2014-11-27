class Stack:
        def __init__(self):
		self.items = []
        def is_empty(self):
               	return self.items ==[]
        def push(self, item):
                self.items.insert(0, item)
        def pop(self):
                return self.items.pop(0)
	def peek(self):
                return self.items[0]
        def size(self):
                return len(self.items)
def reverse_str(my_str):
	b = []
	m = Stack()
	a_stack = list(my_str)
	for i in range(len(a_stack)):
	      m.push(a_stack[i])
	#print m.is_empty()
	for j in range(len(a_stack)):
		b.append(m.pop())
	print "".join(b)
reverse_str("reversed string")

	 
	 


