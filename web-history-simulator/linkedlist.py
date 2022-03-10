
from node import Node

class LinkedList:
	
	def __init__(self):
		self._front = None
		self._back = None
		self._length = 0
	
	def get_length(self):
		return(self._length)
		
	def get_node_at(self, index):
		if self.valid_index(index):
			jumper = self._front
			if index == 0:
				return (jumper)
			elif (index == self.get_length() - 1):
				back_copy = self._back
				return(back_copy)
			else:
				for i in range(index):
					jumper = jumper.next
				return(jumper)
		else:
			raise IndexError("IndexError: cannot get_node_at, at an invalid index")
			
		
	def get_entry(self, index):
		try:
			return (self.get_node_at(index).data)
		except IndexError as e:
			return(e)
			
	def is_empty(self):
		return (self._front == None)
	
	def insert(self, index, entry):
		
		new_node = Node(entry)
		
		if self.valid_index(index):
		
			if self.is_empty():
				
				self._front = new_node
				self._back = new_node
				
			else:
				
				if index == 0:
					new_node.next = self._front
					self._front = new_node
					
				elif index == self._length:
					self._back.next = new_node
					self._back = new_node
					
				else:
					before = get_node_at(index - 1)
					new_node.next = before.next
					before.next = new_node
				
			self._length = self._length + 1
			
		else:
			raise IndexError(f"IndexError: index {index} is out of range.")
	
	def valid_index(self, index):
		return ((index >= 0) and (index <= self._length))
	
	def remove(self, index):
		
		if self.valid_index(index):
			
			if self.is_empty():
				raise RuntimeError("RuntimeError: cannot remove on an empty list")
				
			else:
				if (index == 0):
					self._front = self._front.next
					
				elif (index == self.get_length() - 1):
					target = self.get_node_at(index - 1)
					self._back = target
					target.next = None
					
				else:
					before = self.get_node_at(index - 1)
					after = self.get_node_at(index + 1)
					before.next = after
				self._length = self._length - 1
			
		else:
			raise IndexError(f"IndexError here: index {index} is out of range.")
	
	def clear(self):
		self._front = None
		self._back = None
	
	
	
	
	
	




























