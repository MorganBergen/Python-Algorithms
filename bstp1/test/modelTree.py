

from re import L
from node import Node

class BSTMap:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.bstSearch(self.root, key) != None
    
    def valueOf(self, key):
        node = self.bstSearch(self.root, key)
        return node.data

    def bstSearch(self, subtree, target):
        if subtree == None:
            return(None)
        elif target < subtree.data:
            return self.bstSearch(subtree.left)
        elif target > subtree.data:
            return self.bstSearch(subtree.right)
        else:
            return subtree
    
    def add(self, key):
        node = self.bstSearch(key)
