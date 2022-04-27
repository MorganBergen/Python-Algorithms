'''
@file		three.py
@author		Morgan Bergen
@date	    April 27 2022
@brief	    the following are the implementation details that will test the time complexity of dequeue() for Queue ADT
            by utilizing this class the following will happen
            1.  a queue will enqueue(data) 1,000 elements into the queue
            2.  a record of the time to perform dequeue() n times will be recorded
            3.  step 1 and 2 will be repeated, increasing the size by 1,000 each time untill the queue has enqueued 100,000 elements
'''

from importlib.resources import path
from queue import Queue
import time

class Three:

    '''
    @pre	    constructor must have been called
    @post		member variables will have been initialized to their defaults, which will be one empty queue and two empty lists
    @param		None
    @raises		None
    @returns	None
    '''
    def __init__(self):
        self.line = Queue()
        self.time = []
        self.n = []


    '''
    @pre	    Three() and execute() must have already been called
    @post		p_queue will have allocated n many elements into the queue
    @param		p_queue, n
    @raises		None
    @returns	None
    '''
    def enqueue_n(self, p_queue, n):
        for i in range(n):
            p_queue.enqueue(i)

    '''
    @pre	    Three() must have already been called
    @post		self.line will have pushed 100,000 elements and allocated the time complexity for each dequeue()
    @param		None
    @raises		None
    @returns	None
    '''
    def execute(self):
        for i in range(100):
            n = (i+1)*1000
            self.enqueue_n(self.line, n)
            print(f"enqueued {self.line.size} nodes to the queue")
            cur = self.line.size
            print(f"__________________________________________")
            self.test_dequeue_n(self.line, cur)
            print(f"__________________________________________")
            print(f"dequeued {cur} nodes to the queue")
            self.line = Queue()
            print('\n')

    '''
    @pre	    Three() and execute()
    @post		p_queue will have dequeued n many times and member variables time 
                and n will have recorded the time complexity of that operation
    @param		p_queue, n
    @raises		RuntimeError if there is an attempt to dequeue() on an already empty queue
    @returns	None
    '''
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
        self.time.append(str(self.nanosec_to_sec(end_time-start_time)))
        self.n.append(str(num_iterations))

    '''
    @pre	    test_dequeue_n() must have already been called
    @post		will convert nano seconds o seconds
    @param		ns
    @raises		None
    @returns	ns/billion
    '''
    def nanosec_to_sec(self, ns):
        billion = 1000000000
        return (ns/billion)
    

    '''
    @pre	   All methods above must have been called
    @post	   a file will be written into a directory which stores the time complexity statitics
    @param	   p_name
    @raises    None
    @returns   None
    '''
    def generate_statistics(self, p_name):
        f = open(p_name, 'w')
        f.writelines("time in seconds\n")
        for i in range(len(self.time)):
            f.writelines(self.time[i])
            f.writelines("\n")

        f.writelines("\nsize of n\n")
        for i in range(len(self.n)):
            f.writelines(self.n[i])
            f.writelines("\n")
        f.close()