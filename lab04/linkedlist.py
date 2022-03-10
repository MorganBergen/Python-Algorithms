
from node import Node

class LinkedList:
	
	def __init__(self):
		self._front = None
		self._back = None
		self._length = 0
		
	def length(self):
		jumper = self._front
		self._length = 0
		while jumper != None:
			jumper = jumper.next
			self._length = self._length + 1
		return(self._length)
	
	'''
	Insert the entry at the index. Valid indices range from 0 to length inclusively.
	Inserting at index = 0 inserts at the front.
	Inserting at entry index=length adds to the back.
	Each insert increases the length by 1.
	'''
	def insert(self, index, entry):
		valid = (index >= 0) and (index <= self._length)
		if valid:
			new_node = Node(entry)
			if index == 0:
				self._front = new_node
				self._front.next = None
			elif (index == self._length):
				self._back.next = new_node
				self._back = new_node
			
			else:
				print()
				
			
			
		else:
			raise IndexError(f"IndexError: index {index} is out of range.")
		
