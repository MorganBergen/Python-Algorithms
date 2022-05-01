


from node import Node

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

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
    
#	def insert(self, data)
