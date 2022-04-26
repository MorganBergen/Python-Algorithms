
from queue import Queue

class Three:
    def __init__(self):
        self.line = Queue()
        






 





'''
1.  enqueue 1,000 elements
2.  record time to perform dequeue 1,000 elements
3.  enqueue 2,000 elements
4.  record time to perform dequeue 2,000 elements
...
3.  enqueue 100,000 elements
4.  record time to perform dequeue 100,000 elements
'''



'''

import time

def nanosec_to_sec(ns):
	billion = 1000000000 # one thousand million
	return (ns/billion)

def main():
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

if __name__ == "__main__":
	main()

    def basic(self):
        print(f"is the line empty? ", end="")
        print(self.line.is_empty())
        self.line.enqueue("morgan")
        self.line.enqueue("maha")
        self.line.enqueue("bergen")
        print(f"new front {self.line.dequeue()}")
        print(f"is the line empty? ", end="")
        print(self.line.is_empty())
        print(f"front -> [{self.line.peek_f()}]")
        print(f"[{self.line.peek_b()}] <- back")
'''