
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        # self._head = None change to this when you are done
        self.size = 0

    def is_empty(self):
        return (self.head == None)

    


    

    def get_node_at(self, index):
        target = self.head
        for i in range(index):
            target = target.next
        return target

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

    def print(self):
        cur = self.head
        if self.is_empty():
            print("list is empty")
        while cur != None:
            if cur.next == None:
                print(f"{cur.data} -> • ")
            else:
                print(f"{cur.data} -> ", end="")   
            cur = cur.next

# 	def print_list(self):
# 		current = self.head
# 		if self.is_empty():
# 			print("list is empty")
# 		counter = 0
# 		while counter < self.length:
# #			print(f"{counter} -> ", end="")
# 			counter = counter + 1
# 		print()
# 		while current != None:
# 			print(f"{current.data} -> ", end="")
# 			current = current.next
# #		print(f"\nlength = {self.length}")
