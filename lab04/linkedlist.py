
from node import Node

class LinkedList:
	
	def __init__(self):
		self._front = None
		self._length = 0
		
	def length(self):
		jumper = self._front
		length = 0
		while jumper != None:
			jumper = jumper.next
			length = length + 1
		if length == self._length:
			return(self._length)
	
	
