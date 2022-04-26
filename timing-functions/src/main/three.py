
from queue import Queue
import time

class Three:
    def __init__(self):
        self.line = Queue()

    def enqueue_n(self, p_queue, n):
        for i in range(n):
            p_queue.enqueue(i)

    def execute(self):
        for i in range(100):
            n = (i+1)*1000
            self.enqueue_n(self.line, n)
            print(f"enqueued {self.line.size} nodes to the queue")
            print(f"__________________________________________")
            self.test_dequeue_n(self.line, self.line.size)
            print(f"__________________________________________")
            print(f"dequeued {self.line.size} nodes to the queue")
            self.line = Queue()
            print('\n')

    def test_dequeue_n(self, p_queue, n):
        print("beginning the timing code...")
        num_iterations = n
        start_time = time.process_time_ns()

        try:
            print(f"size before dequeue {p_queue.size}")
            for i in range(num_iterations):
                p_queue.dequeue()
            print(f"size after dequeue {p_queue.size}")
        except RuntimeError as e:
            print(e)

        end_time = time.process_time_ns()
        print(f"total iterations: ", num_iterations)        
        print(f"total time in nano seconds: ", end_time-start_time)
        print(f"total time in seconds: ", self.nanosec_to_sec(end_time-start_time))
        return None

    def nanosec_to_sec(self, ns):
        billion = 1000000000
        return (ns/billion)
    
    '''
    def test_n(self, p_queue, n):
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


 

    def nanosec_to_sec(self, ns):
    	billion = 1000000000 # one thousand million
    	# return(ns/billion)

    '''



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