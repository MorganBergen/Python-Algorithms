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

def main():
	cards = Stack()
	print(f"is empty? {cards.is_empty()}")
	cards.push('queen')
	try:
		print(f"peek at top? {cards.peek()}")
	except RuntimeError as e:
		print(e)
	cards.push('jack')
	try:
		print(f"peek at top? {cards.peek()}")
	except RuntimeError as e:
		print(e)
	cards.push('joker')
	try:
		print(f"peek at top? {cards.peek()}")
	except RuntimeError as e:
		print(e)
	print(f"is empty? {cards.is_empty()}")
	
	
	
		
	

if __name__ == "__main__":
	main()

