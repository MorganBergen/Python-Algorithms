



def add(self, entry):

	if self._root == None:
		self._root = BNode(entry)
	
	elif self._root.entry < entry: # check to add right
		if self._root._right == None:
			self._root._right = BNode(entry)
		else:
			self._rec_add(entry, self._root.right)
			
	elif self._root.entry > entry: # check to add left
		if self._root._left == None:
			self._root._left = BNode(entry)
		else:
			self._rec_add(entry, self._root.left)
	else:
		raise RuntimeError('No Duplicates Allowed')

def _rec_add(self, entry, cur_node):
	
	if cur_node == None:
	
		self.cur_node = BNode(entry)
	
	else:
		if cur_node.entry < entry:
		
			if cur_node.right == None:
				cur_node._right = BNode(entry)
			else:
				self._rec_add(entry, cur_node.right)
		elif cur_node.entry > entry:
			if cur_node.left == None:
				cur_node._left = BNode(entry)
			else:
				self._rec_add(entry, cur_node.left)
		else:
		
		raise RuntimeError("no duplicates allowed")



'''

tree = Tree()
	tree.add(1, "a")
	tree.add(2, "b")
	tree.add(3, "c")
	tree.add(4, "d")
	tree.add(5, "e")
	tree.add(6, "f")
	print(tree.root.data)
	
	try:
		tree.add(1, "string")
	except RuntimeError as e:
		print(e)
	
	print(f"in order traversal")

	tree.inorder(tree.root)

	print(f"pre order traversal")
	tree.preorder(tree.root)
class Node:
	def __init__(self, key, data):
		self.key = key
		self.data = data
		self.left = None
		self.right = None

def nodetester():
	root = Node(4, "d")
	root.left = Node(2, "b")
	root.right = Node(6, "f")
	root.left.left = Node(1, "a")
	root.left.right = Node(3, "c")
	root.right.left = Node(5, "e")
	root.right.right = Node(7, "g")





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
            self.root = self.insert(self.root, key, data)
            self.size += 1
        else:
            raise RuntimeError("cannot insert duplicate key values")
            
    def insert(self, subtree, key, data):
        if subtree == None:
            subtree = Node(key, data)
        
        elif key < subtree.key:
            subtree.left = self.insert(subtree.left, key, data)
        
        elif key > subtree.key:
            subtree.right = self.insert(subtree.right, key, data)
        
        return subtree
 
 '''

        


















