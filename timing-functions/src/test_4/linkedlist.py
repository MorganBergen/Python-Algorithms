'''
@file		linkedlist.py
@author		Morgan Bergen
@date		April 27 2022
@brief		This is a contemporary node based implementation of this linkedlist data structure.  The following outlines the general functionality of 			each memeber method of this class.

def __init__(self)
- Initializes an empty linkedlist with a length of 0.

def get_length(self)
- Return length of the list

def insert(self, index, entry)
- Insert the entry at the index.
- Valid indices range from 0 to length inclusively.
- Inserting at index=0 inserts at the front.
- Inserting at index=length adds to the back.
- Each insert increases the length by 1.

def remove(self, index)
- Removes the entry at the index.
- Valid indices range from 0 to length - 1 inclusively.
- Each remove decreases the length by 1.

def is_empty(self)
- Returns true if self._front refers to nothing.

def get_node_at(self, index)
- traverses through the linked list to a given index
- returns a reference to a node at that given parameterized index

def get_entry(self, index)
- Return the entry at index, raises a RuntimeError otherwise.

def clear(self)
- Empties the list

def set_entry(self, index, entry)
- Sets the entry at index, raises a RuntimeError otherwise.
- Even if successful, the length remains the same.
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
	@post
	@param		None
	@raises		None
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
	@pre		LinkedList() object must be allocated from a seperate module
	@post
	@param		None
	@raises		None
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

    def clear(self):
        if self.is_empty():
            raise RuntimeError("error: linkedList is already empty")
        else:
            self.head = None
        self.size = 0

    def get_data(self, index):
        return(self.get_node_at(index).data)

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

    def get_node_at(self, index):
        self.iterations_for_get = 0
        target = self.head
        for i in range(index):
            target = target.next
            self.iterations_for_get += 1
        return target


