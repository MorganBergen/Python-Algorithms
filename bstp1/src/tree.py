

from node import Node

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def manualAdd(self, data):
        self.root = Node(data)
        self.size += 1
	    

    def print_tree(self):
        print(f"	[{self.root.data}]")
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
