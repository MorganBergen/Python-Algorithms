
from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0


	'''
	@pre		a queue must exist
	@post		None
	@param		None
	@raises		None
	@returns	a boolean stating weather the front and back of the queue is refering to None or not.
	'''
    def is_empty(self):
        return(self.front == None and self.back == None)

	
	'''
	@pre		Queue() must have been constructed
	@post		None
	@param		None
	@raises		RuntimeError
	@returns	self.front.data
	'''
    def peek_f(self):
        if self.is_empty():
            raise RuntimeError("error: cannot peek front on an empty queue")
        else:
            return(self.front.data)

	'''
	@pre		Queue() must have been constructed
	@post		None
	@param		None
	@raises		RuntimeError
	@returns	self.back.data
	'''
    def peek_b(self):
        if self.is_empty():
            raise RuntimeError("error: cannot peek back on an empty queue")
        else:
            return(self.back.data)     
    
	'''
	@pre		Queue() must have been constructed
	@post		a node is added to the back of the queue
	@param		data
	@raises		None
	@returns	None
	'''
    def enqueue(self, data):
        new_back = Node(data)
        if self.is_empty():
            self.back = new_back
            self.front = new_back
        else:
            self.back.next = new_back
            self.back = new_back
            self.back.next = None
        self.size += 1

	'''
	@pre		Queue() must have been constructed and cannot be empty
	@post		an element is removed from the queue
	@param		None
	@raises		RuntimeError
	@returns	the previous data value that was removed
	'''
    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("error: cannot dequeue on an empty stack")
        
        elif self.front.next == None:
            self.front = None
            self.back = None
            self.size -= 1        
        else:
            self.front = self.front.next
            self.size -= 1
            return (self.front.data)
