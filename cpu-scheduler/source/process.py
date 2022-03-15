'''
@file		process.py
@author		Morgan Bergen
@date		March 4 2022
@brief		This is the process class
			a process contains a call stack, which is a stack of function names, a process is in charge of managing its call stack by either making additional calls (adding to the call stack) or having a function return (removing from the call stack)
			START <process name>
			e.g. START itunes
			e.g. START firefox
			a new process is created and added to the queue
			all processes start with a "main" as their first function call.
			print a message to the screen indictating which process was added to the queue
			The member variables consist of a stack object and the name of the program
			The member methods consist of call_adding which pushes an element onto the stack, specifically a function name.
			As well as call_removing which tries to pop() a node off a call stack, if the stack is empty it will catch an exception of the type runtimeerror or attribution error, and will display a message.
'''

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
