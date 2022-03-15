from this import d
from stack import Stack
from node import Node

class Queue:

    def __init__(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front == None
    
    def peek_front(self):
        if self.is_empty():
            raise RuntimeError('Queue Empty')
        else:
            return self.front.data

    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.top = node
            self.back = node
        else:
             self.back.next = node
             self.back = node
             self.back.next = None
        message = f"{self.back.data.name} has been added to the queue"
        return message

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError('Queue Empty')
        elif self.front.next == None:
            self.front.next = None
            self.back.next == None
        else:
            self.front = self.front.next
            return self.front.data
