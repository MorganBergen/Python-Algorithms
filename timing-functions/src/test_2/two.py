'''
@file		two.py
@author		Morgan Bergen
@date		April 27 2022
@brief	    these is the implementation details that will test the time complexity of all possible pop() for ADT stack
            by utilizing this class the following will happen
            1.  a stack will push() 1,000 elements onto the stack
            2.  a record of the time to perform a pop() of size n with the stack will be stored into a list
            3.  step 1 and 2 will be repeated, increasing the size by 1,000 each time untill the stack has pushed 100,000 times
'''

import time
from stack import Stack

class Two:

    '''
    @pre	    constructor must have been called
    @post		member variables will have been initialized to their defaults, which will be empty data structures
    @param		None
    @raises		None
    @returns	None
    '''
    def __init__(self):
        self.pile = Stack()
        self.time = []
        self.n = []

    '''
    @pre	    Two() and execute() must have been called
    @post		will generate a file holding all of the time complexity statistics for n from 1,000 - 100,000
    @param		p_name
    @raises		None
    @returns	None
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
    
     
    '''
    @pre	    Two() and execute() must have been called
    @post		self.pile have pushed n amount of elements onto the stack
    @param		p_stack, n
    @raises		None
    @returns	None
    '''
    def push_n(self, p_stack, n):
        for i in range(n):
            p_stack.push(i)

    '''
    @pre	    Two() must have been already called
    @post		time complexity statistics will be recorded for 100,000 pop()
    @param		None
    @raises		None
    @returns	None
    '''
    def execute(self):
        for i in range(100):
            n = (i+1)*1000
            self.push_n((self.pile), n)
            print(f"pushed {self.pile.size} nodes to the stack")
            print(f"current size = {self.pile.size}")
            cur = self.pile.size
            print(f"_____________________________________________")
            self.test_n(self.pile, self.pile.size)
            print(f"_____________________________________________")
            print(f"popped {cur} nodes off the stack")
            print(f"updated size = {self.pile.size}")
            self.pile = Stack()
            print("\n")

    '''
    @pre	    test_n() must have already been called
    @post		converts nano seconds to seconds
    @param		ns
    @raises		None
    @returns	ns/billion
    '''
    def nanosec_to_sec(self, ns):
        billion = 1000000000
        return (ns/billion)    

    '''
    @pre	    One() and execute() must have already been called
    @post	    lists n and time will be initialized with time complexity statistics
    @param		p_stack, n
    @raises		RuntimeError if there is an attempt to pop() an empty stack
    @returns	None
    '''
    def test_n(self, p_stack, n):
        print("beginning the timing code...")
        num_iterations = n
        start_time = time.process_time_ns()

        try:
            for i in range(num_iterations):
                p_stack.pop()
        except RuntimeError as e:
            print(e)
        
        end_time = time.process_time_ns()
        print(f"total iterations: ", num_iterations)
        print(f"total time in nano seconds: ", end_time-start_time)
        print(f"total time in seconds: ", self.nanosec_to_sec(end_time-start_time))
        self.time.append(str(self.nanosec_to_sec(end_time-start_time)))
        self.n.append(str(num_iterations))
