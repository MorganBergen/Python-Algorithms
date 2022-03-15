from node import Node

class Stack:
	
	def __init__(self):
		self.top = None
	
	def is_empty(self):
		return self.top == None
	
	def push(self, data):
		node = Node(data)
		if self.is_empty():
			self.top = node
		
		else:
			node.next = self.top
			self.top = node
	
	def peek(self):
		if self.is_empty():
			raise RuntimeError('Stack Empty')
		else:
			return self.top.data

	def pop(self):
		if self.is_empty():
			raise RuntimeError('Stack Empty')
		else:
			self.top = self.top.next
			return self.top
