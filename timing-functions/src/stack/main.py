import time
from stack import Stack

def nanosec_to_sec(ns):
	billion = 1000000000 # one thousand million
	return (ns/billion)

def test():
	print("beginning the timing code...")
	num_iterations = 100000000 # one hundred million
	start_time = time.process_time_ns()

	# loop that does nothing but repeat, hence the _ variable and the keywork pass
	# which just means do nothing

	for _ in range(num_iterations):
		pass

	end_time = time.process_time_ns()
	
	print(f"total time in nano seconds: ", end_time-start_time)
	print(f"total time in seconds: ", nanosec_to_sec(end_time-start_time))

def test_pop(p_stack):
	print("beginning the timing code...")
	num_iterations = 1 # one
	start_time = time.process_time_ns()
	
	
	try:
		for i in range(num_iterations):
			p_stack.pop()
	except RuntimeError as e:
		print(e)
		
	end_time = time.process_time_ns()
	print(f"total time in nano seconds: ", end_time-start_time)
	print(f"total time in seconds: ", nanosec_to_sec(end_time-start_time))


def main():
	
	pile = Stack()
		
#	for i in range(10):
#		for j in range((i+1)*1000):
#			pile.push(j)
#		test_pop(pile)
#		print()

	i = 1
	for i in range(11):
		j = 1
		for j in range(1001):
			pile.push(j*i)
		test_pop(pile)
	print(f"[{pile.peek()}] <- top")
			


if __name__ == "__main__":
	main()
	
	
	
	
	
'''
You will fill each data structure with an increasing number of elements and record a time for each. For each method, start with a data size of 1000 then increase by 1000, recording another time, and repeat until you've reached 100,000 elements.

For example.

Let's say I want to time Pop for a Stack.

I would do the following:

1. Fill a stack with 1000 elements

2. Record time to perform a single pop with that size stack

3. Fill a stack with 2000 elements

4. Record a time to perform a single pop with that size stack

5. Repeat these steps, increasing the size by 1000 each time until I've recorded a time for a stack with 100,000 elements in it
'''

	
	
	
	
	
	
	
	

