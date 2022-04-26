import time
from stack import Stack

def nanosec_to_sec(ns):
	billion = 1000000000 # one thousand million
	return (ns/billion)

def test_pop(p_stack, amount):
	print("beginning the timing code...")
	num_iterations = amount # one
	start_time = time.process_time_ns()
	
	try:
		for i in range(num_iterations):
			p_stack.pop()
		print(f"{num_iterations} node has been popped off the stack of size {p_stack.size}")

	except RuntimeError as e:
		print(e)
		
	end_time = time.process_time_ns()
	print(f"total time in nano seconds: ", end_time-start_time)
	print(f"total time in seconds: ", nanosec_to_sec(end_time-start_time))

def push_amount(p_stack, amount):
	for i in range(amount):
		p_stack.push(i)

def main():
	
	pile = Stack()
		
	for i in range(100):
		print("\n")
		push_amount(pile, (i+1)*1000)
		print(f"current size = {pile.size}")
		print(f"____________________________________________")
		test_pop(pile, 1)
		print(f"____________________________________________")
		print(f"final size = {pile.size}")
		pile = Stack()

if __name__ == "__main__":
	main()
	
