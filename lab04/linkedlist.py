
from node import Node

class LinkedList:
	
	def __init__(self):
		self._front = None
		self._back = None
		self._length = 0
	
	def get_length(self):
		return(self._length)
		
	def get_node_at(self, index):
		jumper = self._front
		
		for i in range(index):
			jumper = jumper.next
		
		return(jumper)
			
	def insert(self, index, entry):
		if self.valid_index(index):
			new_node = Node(entry)
			if index == 0:
				self._front = new_node
				self._front.next = None
			elif (index == self._length):
				self._back.next = new_node
				self._back = new_node
			else:
				before = get_node_at(index - 1)
				after = before.next
				before.next = new_node
				new_node.next = after
				
			self._length = self._length + 1
		else:
			raise IndexError(f"IndexError: index {index} is out of range.")
	
	def valid_index(self, index):
		return (index >= 0 and index <= self._length)






