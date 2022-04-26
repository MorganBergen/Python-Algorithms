
from node import Node

class Stack:
	
	def __init__(self):
		self._top = None
		self.size = 0
		
	def push(self, data):
		if self.is_empty():
			self._top = Node(data)
			self.size += 1
		else:
			new_node = Node(data)
			new_node.next = self._top
			self._top = new_node
			self.size += 1
		
	def pop(self):
		if self.is_empty():
			raise RuntimeError("error: cannot pop on an empty stack")
		else:
			old = self._top.data
			self._top = self._top.next
			self.size = self.size - 1
			return (old)
			
	def peek(self):
		if self.is_empty():
			raise RuntimeError("error: cannot peak on an empty stack")
		else:
			return (self._top.data)
		
	def is_empty(self):
		if self._top == None:
			return True
		else:
			return False
