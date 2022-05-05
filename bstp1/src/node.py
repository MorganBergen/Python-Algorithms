
class Node:
    def __init__(self, key, data):
        self.data = data
        self.key = key
        self.left = None
        self.right = None

'''
    
    def search(self, subtree, target):
        

        if subtree == None:
            return None

        print(f"data {subtree.data}, key {subtree.key}, target {target}")
        print(subtree.data, subtree.key, target)

        if target < subtree.key:
            return self.search(subtree.left)
        
        elif target > subtree.key:
            return self.search(subtree.right)
        elif target == subtree.key:
            raise RuntimeError("cannot insert duplicates")

        else:
            return subtree
'''