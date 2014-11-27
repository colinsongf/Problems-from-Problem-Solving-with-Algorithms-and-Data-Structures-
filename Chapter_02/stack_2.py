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
#s = Stack()
#s.push("hello")
#s.push("true")
#print(s.pop())
import stack
def reverse_string(my_str):
	s = ""
	m = Stack()
	a_stack = list(my_str)
	while not m.is_empty():
	      s + m.pop()
	print s
