import time
from stack import Stack

class OperationOne:

    def __init__(self):
        self.pile = Stack()
    
    def push_n(self, p_stack, n):
        for i in range(n):
            p_stack.push(i)

    def execute(self):
        for i in range(100):
            n = (i+1)*1000
            self.push_n((self.pile), n)
            print(f"pushed {self.pile.size} nodes to the stack")
            print(f"stack size = {self.pile.size}")
            print(f"_____________________________________________")
            self.test_n(self.pile, 1)
            print(f"_____________________________________________")
            print(f"popped {1} node off the stack")
            print(f"stack size = {self.pile.size}")
            self.pile = Stack()


    def nanosec_to_sec(self, ns):
        billion = 1000000000
        return (ns/billion)    

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
        print(f"total time in nano seconds: ", end_time-start_time)
        print(f"total time in seconds: ", self.nanosec_to_sec(end_time-start_time))