
import time
from stack import Stack

class OperationOne:
	
	def __init__(self):
		pile = Stack()
	
	def execute(self):
		for i in range(100):
		print("\n")
	
	def test(p_stack, n):
		print("beginning the timing code...")
		num_iterations = n
		start_time = time.process_time_ns()
		
		try:
			for i in range(num_iterations):
				p_stack.pop()
		except RuntimeError as e:
		print(e)
	
	end_time = time.process_time_ns()
	print(f"total time in nano seconds: ", end_time-start_time)
	print(f"total time in seconds: ", nanosec_to_sec(end_time-start_time))
	
	def nanosec_to_sec(ns):
		billion = 1000000000
		return(ns/billion)
