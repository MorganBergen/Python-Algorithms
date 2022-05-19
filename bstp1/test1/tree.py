

from node import Node

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, data):
        
        if self.root == None:
            self.root = Node(data)
            print(f"root -> ", self.root.data)
            self.size += 1
        elif data > self.root.data:
            if self.root.right == None:
                self.root.right = Node(data)
                print(self.root.right.data)
            else:
                print("rec_add")
        
            self.size += 1

        elif data < self.root.data:
            if self.root.left == None:
                self.root.left = Node(data)
            else:
                print("rec add")
            self.size += 1
        else:
            raise RuntimeError("no duplicates allowed")

    def print_tree(self):
        print(f"	[{self.root.data}]")
        print(f"	[{self.root.right.data}]")
	    # print(f"	/ \	")
	    # print(f"     [{self.root.data}]   [{self.root.right.data}]")


    def preorderTrav(self, subtree):
        if subtree != None:
            print(subtree.data)
            self.preorderTrav(subtree.left)
            self.preorderTrav(subtree.right)
    
    def inorderTrav(self, subtree):
        if subtree != None:
            self.inorderTrav(subtree.left)
            print(subtree.data)
            self.inorderTrav(subtree.right)
    
    def postorderTrav(self, subtree):
        if subtree != None:
            self.postorderTrav(subtree.left)
            self.postorderTrav(subtree.right)
            print(subtree.data)

    def __len__(self):
        return (self.size)



'''
    
    def search(self, target): 
        return self._rec_search(target, self.root)

    def rec_search(self, target, cur_node): #change to _rec_search first
        # you will define
        # find your base case first
        # deal with cur_node being None first
        return (target, cur_node)
'''
