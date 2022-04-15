'''
@file		queue.py
@author		Morgan Bergen
@date		March 4 2022
@brief		This is the queue class
			The queue class is in charge of organizing the stacks.
			The member variables consist of front and back node references.
			The member methods consist of the following,
			enqueue(data) puts the entry at the front of the Queue.
			dequeue() Remove and return the value at the front of the Queue. Raise RuntimeError otherwise
			peek_front() Return value at the front of the queue, raise a RuntimeError otherwise.
			is_empty() Return True if Queue is empty, False otherwise.
			peek_front_stack
'''


from stack import Stack
from node import Node

class Queue:
	
	'''
	@pre		a schedule must be constructed
	@post		the front and the back of the stack is refering to none
	@param		None
	@raises		None
	@returns	None
	'''
	def __init__(self):
		self.front = None
		self.back = None

	'''
	@pre		a queue must exist
	@post		None
	@param		None
	@raises		None
	@returns	a boolean stating weather the front of the queue is refering to None or not.
	'''
	def is_empty(self):
		return self.front == None
		
	'''
	@pre		a queue must exist
	@post		a node is added to the back of the queue
	@param		data
	@raises		None
	@returns	None
	'''
	def enqueue(self, data):
		node = Node(data)
		if self.is_empty():
			self.front = node
			self.back = node
		else:
			self.back.next = node
			self.back = node
			self.back.next = None

	'''
	@pre		a queue must exist
	@post		None
	@param		None
	@raises		RuntimeError
	@returns	self.front.data
	'''
	def peek_front(self):
		if self.is_empty():
			raise RuntimeError('Queue Empty')
		else:
			return self.front.data
			
			
	'''
	@pre		a queue must exist
	@post		the stack is removed from the front of the queue
	@param		None
	@raises		RuntimeError
	@returns	the previous data value that was removed
	'''
	def dequeue(self):
		if self.is_empty() == True:
			raise RuntimeError('Queue Empty')
		elif self.front.next == None:
			self.front = None
			self.back = None
		else:
			temp = self.front.data
			self.front = self.front.next
			return (temp)
			
			
			
			
			
			
			
			
			
			
			
			


	
