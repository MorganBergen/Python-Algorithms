'''
@file		cpu_scheduler.py
@author		Morgan Bergen
@date		March 4 2022
@brief		This is the cpu_scheduler class
			The CPU_Scheduler is in charge of adding Processes to a Queue, allowing them CPU time, then moving them to the back of the queue if they need.
'''

from process import Process
from stack import Stack
from queue import Queue

class Cpu:
	
	'''
	@pre		Cpu() must be called
	@post		Queue data structure gets created
	@param		None
	@raises		None
	@returns	None
	'''
	def __init__(self):
		self.scheduler = Queue()
	
	'''
	@pre		file must exist and be of the correct name
	@post		"START" command is read in:
				- the name of the process gets added to the queue
				- the Process constructor is called and via the constructor a new stack is created
				- a message is printed to the console stating that the program has been added to the queue
				
				"CALL" command is read in:
				- a message is printed to the console stating that the name of the progcess at the front of the queue has called the function
				- the function is added at the top of the stack to the front most stack in the queue
				- then the process is removed from the front and added to the back of the queue.
				
				"RETURN" command is read in:
				- if the process at the front of the queue has additional functions other than main that call-stack returns
				- if the process has any functions left on the call stack it is moved to the back of the queue
				- if the process has a main at the top of it's stack then the process gets removed and a messgae will be consoled out to the user stating that this occured
				- if the process ends a message will be consoled output that the process ended
	@param		p_file, note:  we are assuming good input from the file
	@raises		None
	@returns	None
	'''
	def fileIO(self, p_file):
		inFile = open(p_file)
		
		for line in inFile:
			command = line.split()
			
			if command[0] == 'START':
				self.scheduler.enqueue(Process(command[1]))
				print(f"{command[1]} has been added to the queue")
			
			elif command[0] == 'CALL':
				
				print(f"{self.scheduler.peek_front().name} calls {command[1]}")
				self.scheduler.peek_front().stack.push(command[1])
				self.scheduler.enqueue(self.scheduler.dequeue())
			
			elif command[0] == 'RETURN':
				if self.scheduler.is_empty():
					print("Queue is Empty")
					
				else:
					if self.scheduler.peek_front().stack.peek() != "main":
						print(f"{self.scheduler.peek_front().name} returns from {self.scheduler.peek_front().stack.peek()}")
						self.scheduler.peek_front().stack.pop()
						self.scheduler.enqueue(self.scheduler.dequeue())
					elif self.scheduler.peek_front().stack.peek() == "main":
						print(f"{self.scheduler.peek_front().name} returns from {self.scheduler.peek_front().stack.peek()}")
						print(f"{self.scheduler.peek_front().name} process has ended")
						self.scheduler.dequeue()
		
		inFile.close()







