'''
@file		stack.py
@author		Morgan Bergen
@date		April 27 2022
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
	
	'''
	@pre		a stack constructor must be called
	@post		self.top is initialized to none
				self.size is initialized to 0
	@param		None
	@raises		None
	@returns	None
	'''
	def __init__(self):
		self._top = None
		self.size = 0
	
	'''
	@pre		a stack must exits
	@post		a new node is added at the top of the stack
	@param		data
	@raises		none
	@returns	none
	'''
	def push(self, data):
		if self.is_empty():
			self._top = Node(data)
			self.size += 1
		else:
			new_node = Node(data)
			new_node.next = self._top
			self._top = new_node
			self.size += 1
	
	'''
	@pre		a stack must exist
	@post		a node is removed from the top of the stack
	@param		None
	@raises		RuntimeError
	@returns	self._top
	'''
	def pop(self):
		if self.is_empty():
			raise RuntimeError("error: cannot pop on an empty stack")
		else:
			old_node = self._top.data
			self._top = self._top.next
			self.size = self.size - 1
			return (old_node)
	
	'''
	@pre		a stack must exist
	@post		None, the peek method will simply reveal the data value at the top of the stack, if the stack is not empty
	@param		None
	@raises		RuntimeError
	@returns	self.top.data
	'''
	def peek(self):
		if self.is_empty():
			raise RuntimeError("error: cannot peak on an empty stack")
		else:
			return (self._top.data)
	
	'''
	@pre		a stack must exist
	@post		None
	@param		None
	@raises		None
	@returns	a boolean stating whether the there is something at the top of the stack or not
	'''
	def is_empty(self):
		if self._top == None:
			return True
		else:
			return False

