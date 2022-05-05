
from node import Node

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.inorder(self.root)
    
    def inorder(self, subtree):
        if subtree != None:
            self.inorder(subtree.left)
            print(subtree.data, subtree.key)
            self.inorder(subtree.right)

    def preorder(self, subtree):
        if subtree != None:
            print(subtree.data, subtree.key)
            self.inorder(subtree.left)
            self.inorder(subtree.right)
    
    def postorder(self, subtree):
        if subtree != None:
            self.postorder(subtree.left)
            self.postorder(subtree.right)
            print(subtree.data, subtree.key)


    
    









    def add(self, key, data):
        if self.root == None:
            self.root = Node(key, data)

        elif self.root.key > key:      #check left
            if self.root.left == None:
                self.root.left = Node(key, data)
            else:
                self.rec_add(self.root.left, key, data)
        elif self.root.key < key:       #check right
            if self.root.right == None:
                self.root.right = Node(key, data)
            else:
                self.rec_add(self.root.right, key, data)
        else:
            raise RuntimeError("No duplicates allowed")


    def rec_add(self, cur_node, key, data):
        if cur_node == None:
            self.cur_node = Node(key, data)
        else:
            if cur_node.key > key: 
                if cur_node.left == None:
                    cur_node.left = Node(key, data)
                else:
                    self.rec_add(cur_node.left, key, data)
            
            elif cur_node.key < key:
                if cur_node.right == None:
                    cur_node.right = Node(key, data)
                else:
                    self.rec_add(cur_node.right, key, data)
                            
