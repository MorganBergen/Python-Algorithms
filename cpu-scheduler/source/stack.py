'''
@file		stack.py
@author		Morgan Bergen
@date		March 4 2022
@brief		This is the stack class
			Consisting of one memeber variable that refers the top most node in the stack.
			The funtionality of this class consists of the following member methods,
			is_empty() returns true if the stack is empty and false if otherwise
			push(data) removes and retrns the value at the top of the stack, raises a runtimeerror if otherwise.
			peek() returns a value at the top of the stack, raises a runtimeerror if otherwise.
			pop() removes and returns the value at the top of the stack
'''


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
			return(self.top)
