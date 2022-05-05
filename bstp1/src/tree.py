
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
    
    def search(self, subtree, target):
        if subtree == None:
            return None
        
        elif target < subtree.key:
            return self.search(subtree.left)
        
        elif target > subtree.key:
            return self.search(subtree.right)
        
        else:
            return subtree

    def add(self, key, data):
        node = self.search(self.root, key)
        if node != None:
            node = Node(key, data)
            
            return False
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

        

















