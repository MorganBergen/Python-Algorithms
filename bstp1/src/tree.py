


from node import Node

class Tree:
    def __init__(self):
        self.root = None

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
    