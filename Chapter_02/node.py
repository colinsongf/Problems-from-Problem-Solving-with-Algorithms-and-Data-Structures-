class Node:
	def __init__(self, init__data):
		self.data = init__data
		self.next = None
	def get_data(self):
		return self.data
	def get_next(self):
		return self.next
	def set_data(self, new_data):
		self.data = new_data
	def set_next(self, new_next):
		self.next = new_next
temp = Node(93)
print temp.get_data()
	
