
from stack import Stack

class Process:

	def __init__(self, name):
		self.stack = Stack()
		self.name = name
		self.stack.push("main")
		
	def call_adding(self, data):
		self.stack.push(data)
		message = f"{self.name} calls {self.stack.top.data}"
		return(message)
	
	def call_removing(self):
		try:
			self.stack.pop()
		except RuntimeError or AttributeError as e:
			print(e)
