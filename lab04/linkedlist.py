
from node import Node

class LinkedList:
	
	def __init__(self):
		self.front = None
		self.length = 0
		
	def get_length(self):
		jumper = self.front
		self.length = 0
		while jumper != None:
			jumper = jumper.next
			self.length = self.length + 1
			
		return(self.length)
