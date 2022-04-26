
from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return(self.front == None and self.back == None)

    def peek_f(self):
        if self.is_empty():
            raise RuntimeError("error: cannot peek front on an empty queue")
        else:
            return(self.front.data)

    def peek_b(self):
        if self.is_empty():
            raise RuntimeError("error: cannot peek back on an empty queue")
        else:
            return(self.back.data)     
    
    def enqueue(self, data):
        new_back = Node(data)
        if self.is_empty():
            self.back = new_back
            self.front = new_back
        else:
            self.back.next = new_back
            self.back = new_back
            self.back.next = None

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("error: cannot dequeue on an empty stack")
        
        elif self.front.next == None:
            self.front = None
            self.back = None
        
        else:
            self.front = self.front.next
            return (self.front.data)