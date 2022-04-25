
from node import Node

class Stack:
	
	def __init__(self):
		self._top = None
		
	def push(self, data):
		if self.is_empty():
			self._top = Node(data)
			print(f"[{self._top.data}] <- pushed")
		else:
			new_node = Node(data)
			new_node.next = self._top
			self._top = new_node
			print(f"[{self._top.data}] <- pushed")
		
	def pop(self):
		if self.is_empty():
			raise RuntimeError("error: cannot pop on an empty stack")
		else:
			old = self._top.data
			self._top = self._top.next
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


'''

[h] <- Node(h)

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
