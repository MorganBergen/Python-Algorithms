'''
@file		linkedlist.py
@author		Morgan Bergen
@date		April 27 2022
@brief		This is a contemporary node based implementation of a linkedList data structure.
'''

from node import Node

class LinkedList:

	'''
	@pre		LinkedList() object must be allocated from a seperate module
	@post		initializes an empty linkedlist with a size of 0.
				the head of the list initially refers to None
				iterations_for_get is a helper member variable for outside classes
	@param		None
	@raises		None
	@returns	None
	'''
    def __init__(self):
        self.head = None
        self.iterations_for_get = 0
        self.size = 0

	'''
	@pre		LinkedList() object must be allocated from a seperate module
	@post
	@param		None
	@raises		None
	@returns	None
	'''
    def is_empty(self):
        return (self.head == None)

	'''
	@pre		LinkedList() object must be allocated from a seperate module
	@post		will insert an entry at a specified index
				valid indices range from 0 to size inclusively
				inserting at index = 0 inserts a new node at the front of the list
				inserting at index = size adds a new node to the back of the list
				each insert increments the size by 1.
	@param		index, data
	@raises		IndexError if the index is out of range
	@returns	None
	'''
    def insert(self, index, data):
        new_node = Node(data)
        before = self.head

        valid = (index >= 0) and (index <= self.size)

        if valid == True:
            if index == 0:
                new_node.next = self.head
                self.head = new_node
            
            else:
                before = self.get_node_at(index - 1)
                new_node.next = before.next
                before.next = new_node

            self.size += 1

        else:
            raise IndexError("error: index out of range")

	'''
	@pre		LinkedList() object must be allocated from a seperate module and the size of the list must be 1
	@post		removes an entry at the specified index
				valid indices range from 0 to size - 1 inclusively.
				each remove decrements the size by 1.
	@param		index
	@raises		IndexError, RuntimeError
	@returns	None
	'''
    def remove(self, index):
        valid = (index >= 0) and (index <= self.size - 1)

        if self.is_empty():
            raise RuntimeError("error: cannot remove on an empty linkedList")
        
        elif valid == False:
            raise IndexError("error: index out of range")
        
        else:
            if index == 0:
                self.head = self.head.next
            
            else:
                before = self.get_node_at(index - 1)
                after = self.get_node_at(index + 1)
                before.next = after
            self.size -= 1

	'''
	@pre		LinkedList() object must be allocated from a seperate module
				there also must be at least one node in the list / is_empty() must return False
	@post		empties the list by refering the head to None
	@param		None
	@raises		RuntimeError
	@returns	None
	'''
    def clear(self):
        if self.is_empty():
            raise RuntimeError("error: linkedList is already empty")
        else:
            self.head = None
        self.size = 0

	'''
	@pre		LinkedList() construcrtor must have been called
				there also must be at least one node in the list / is_empty() must return False
	@post		None
	@param		index
	@raises		None
	@returns	self.get_node_at(index).data
	'''
    def get_data(self, index):
        return(self.get_node_at(index).data)

	'''
	@pre		LinkedList() construcrtor must have been called
				there also must be at least one node in the list / is_empty() must return False
	@post		None, there will simply be a print out to the consol of each element in the list
	@param		None
	@raises		None
	@returns	None
	'''
    def print_list(self):
        cur = self.head
        if self.is_empty():
            print("list is empty")
        while cur != None:
            if cur.next == None:
                print(f"{cur.data} -> • ")
            else:
                print(f"{cur.data} -> ", end="")
            cur = cur.next

	'''
	@pre		LinkedList() construcrtor must have been called
				there also must be at least one node in the list / is_empty() must return False
	@post		None, this is simply a traversal method to retrive a reference to a node
				at a given specified index position
	@param		index
	@raises		None
	@returns	target
	'''
    def get_node_at(self, index):
        self.iterations_for_get = 0
        target = self.head
        for i in range(index):
            target = target.next
            self.iterations_for_get += 1
        return target



