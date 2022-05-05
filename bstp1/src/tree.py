
from node import Node

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.inorderTrav(self.root)
    
    def inorderTrav(self, subtree):
        if subtree != None:
            self.inorderTrav(subtree.left)
            print(subtree.data)
            self.inorderTrav(subtree.right)
    
    def locate(self, subtree, target):

        if subtree == None:
            return True
        
        elif target < subtree.key:
            return self.locate(subtree.left, target)
        
        elif target > subtree.key:
            return self.locate(subtree.right, target)

        else:
            return False

    def add(self, key, data):

        if self.locate(self.root, key) == True:

        else:
            rasie RuntimeError
        node = self.locate(self.root, key)
        
        if node != None:
            raise RuntimeError("cannot insert duplicate key value")
        else:
            self.root = self.insert(self.root, key, data)
            self.size += 1
            return True

    def insert(self, subtree, key, data):
        if subtree == None:
            subtree = Node(key, data)
        
        elif key < subtree.key:
            subtree.left = self.insert(subtree.left, key, data)
        
        elif key > subtree.key:
            subtree.right = self.insert(subtree.right, key, data)
        
        return subtree

        

















