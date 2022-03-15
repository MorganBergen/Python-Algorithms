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
	
	def __init__(self):
		self.front = None
		self.back = None

	def is_empty(self):
		return self.front == None
		
	def enqueue(self, data):
		node = Node(data)
		if self.is_empty():
			self.front = node
			self.back = node
		else:
			self.back.next = node
			self.back = node
			self.back.next = None
		message = f"{self.back.data.name} has been added to the queue"
		return(message)

	def peek_front(self):
		if self.is_empty():
			raise RuntimeError('Queue Empty')
		else:
			return self.front.data
			
	def dequeue(self):
		
		if self.is_empty() == True:
			raise RuntimeError('Queue Empty')
		elif self.front.next == None:
			self.front.next = None
			self.back.next = None
		else:
			self.front = self.front.next
			return (self.front.data)


	
