
from node import Node

class Stack:
	
	def __init__(self):
		self._top = None
		
	def push(self, data):
		
		if self.is_empty():
			self._top = Node(data)
		else:
			new_node = Node(data)
			new_node.next = self._top
			self._top = new_node
		
	def pop(self):
		return None
	
	def peek(self):
		return None
		
	def is_empty(self):
		if self._top == None:
			return True
		else:
			return False


'''


[h]

[x] <- top
[y]
[z]
[w]
[u]

temp = self.top
temp = [x]
	   [y]
	   [z]
	   [w]
	   [u]
self.top = [h]
self.top.next = temp


'''
