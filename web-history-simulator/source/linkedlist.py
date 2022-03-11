'''
@file		linkedlist.py
@author		Morgan Bergen
@date		March 11 2022
@brief		This is a contemporary node based implementation of this linkedlist data structure.  The following outlines the general functionality of each memeber method of this class.

def __init__(self)
- Initializes an empty linkedlist with a length of 0.

def get_length(self)
- Return length of the list

def insert(self, index, entry)
- Insert the entry at the index.
- Valid indices range from 0 to length inclusively.
- Inserting at index=0 inserts at the front.
- Inserting at index=length adds to the back.
- Each insert increases the length by 1.

def remove(self, index)
- Removes the entry at the index.
- Valid indices range from 0 to length - 1 inclusively.
- Each remove decreases the length by 1.

def is_empty(self)
- Returns true if self._front refers to nothing.

def get_node_at(self, index)
- traverses through the linked list to a given index
- returns a reference to a node at that given parameterized index

def get_entry(self, index)
- Return the entry at index, raises a RuntimeError otherwise.

def clear(self)
- Empties the list

def set_entry(self, index, entry)
- Sets the entry at index, raises a RuntimeError otherwise.
- Even if successful, the length remains the same.
'''

from node import Node

class LinkedList:
	
	def __init__(self):
		self._front = None
		self._back = None
		self._length = 0
	
	def get_length(self):
		return(self._length)
			
	def is_empty(self):
		return (self._front == None)
	
	def get_node_at(self, index):
	
		if (index >= 0) and (index <= self.get_length()):
			jumper = self._front
			if index == 0:
				return jumper
			elif index == self.get_length() - 1:
				back = self._back
				return back
			else:
				for i in range (index):
					jumper = jumper.next
				return jumper
		
		else:
			raise IndexError("Index Error")
		
	def get_entry(self, index):
		return (self.get_node_at(index).data)
		
	def clear(self):
		self._front = None
		self._back = None
	
	def insert(self, index, entry):
		
		new_node = Node(entry)
		
		if (index >= 0) and (index <= self.get_length()):
		
			if self.is_empty():
				self._front = new_node
				self._back = new_node
			
			elif index == 0:
				new_node.next = self._front
				self._front = new_node
			
			elif index == self.get_length():
				self._back.next = new_node
				self._back = new_node
				
			else:
				before = self.get_node_at(index - 1)
				new_node.next = before.next
				before.next = new_node
			
			self._length = self._length + 1
		
		else:
			raise IndexError("IndexError: cannot insert")
	
	def remove(self, index):
		
		if ((index >= 0) and (index <= self._length)):
			
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
			
	def set_entry(self, index, entry):
		
		if index >= self.get_length():
			raise IndexError(f"IndexError: cannot set_entry, {index} > {self.get_length()-1}")
		
		elif index < 0:
			raise IndexError(f"IndexError cannot set_entry, {index} < 0")
			
		elif index == self.get_length() - 1:
			self._back.data = entry
		
		elif index == 0:
			self._front.data = entry
			
		else:
			target = self.get_node_at(index)
			target.data = entry
			
