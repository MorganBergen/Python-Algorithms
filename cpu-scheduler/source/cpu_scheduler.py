'''
@file		cpu_scheduler.py
@author		Morgan Bergen
@date		March 4 2022
@brief		This is the cpu_scheduler class
			The CPU_Scheduler is in charge of adding Processes to a Queue, allowing them CPU time, then moving them to the back of the queue if they need
			The member variables consist of a single queue data structure object
			The member method is fileIO, which is in charge of checking if the file contains a 'START', 'CALL' or 'RETURN' command.  We are assuming good input from the file
'''


from process import Process
from stack import Stack
from queue import Queue

class Cpu:

	def __init__(self):
		self.scheduler = Queue()
		
		
	def fileIO(self, p_file):
		inFile = open(p_file)
		
		for line in inFile:
			command = line.split()
			
			if command[0] == 'START':
				
				print(self.scheduler.enqueue(Process(command[1])))
				
			elif command[0] == 'CALL':
				
				program = self.scheduler.peek_front()
				print(program.call_adding(command[1]))
				
				self.scheduler.dequeue()
				self.scheduler.enqueue(program)
				
			elif command[0] == 'RETURN':
				
				program = self.scheduler.peek_front()
				
				if program.stack.peek() != "main":
					self.schedule.dequeue()
					self.scheduler.enqueue(program)
				elif program.stack.peek() == "main":
					print(f"{program.name} returns from {program.stack.peek()}")
					program.call_removing()
					if program.stack.is_empty() == True:
						print(f"{program.name} process has ended")
		
		inFile.close()
