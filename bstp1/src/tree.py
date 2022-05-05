
from node import Node

class Tree:
	
	def __init__(self):
		self.root = None
		self.size = 0
	
	# visit, left, right
	def preorder(self, subtree):
		print(subtree.key)
		self.preorder(subtree.left)
		self.preorder(subtree.right)
	
	# left, visit, right
	def inorder(self, subtree):
		self.inorder(subtree.left)
		print(subtree.key)
		self.inorder(subtree.right)
		
	# left, right, visit
	def postorder(self, subtree):
		self.postorder(subtree.left)
		self.postorder(subtree.right)
		print(subtree.key)
		
	def __contains__(self, key):
		return (self._search(self.root, key) != None)

	def valueOf(self, key):
		node = self._search(self.root, key)
		if node == None:
			print("invalid key")
		else:
			return (node.data)
		
	def build(self):
		self.root = Node(60, "60 root")
		self.size += 1
		self.root.left = Node(12, "60 root lc")
		self.size += 1
		self.root.right = Node(90, "60 root rc")
		self.size += 1
		self.root.left.left = Node(4, "12s lc")
		self.size += 1
		self.root.left.right = Node(41, "12s rc")
		self.size += 1
		self.root.left.left.left = Node(1, "4s lc")
		self.size += 1
		self.root.left.right.left = Node(29, "41s lc")
		self.size += 1
		self.root.left.right.left.left = (23, "29s lc")
		self.size += 1
		self.root.left.right.left.right = (37, "29s rc")
		self.size += 1
		self.root.right.left = Node(71, "90s lc")
		self.size += 1
		self.root.right.right = Node(84, "90s rc")
		self.size += 1
		self.root.right.right = Node(100, "90s rc")
		self.size += 1
	
	# adds a new entry to the tree or replaces the value of an existing one
	def add(self, key, data):
		# find the ndoe containing the key, if it exists
		node = self._search(self.root, key)
		
		#if the key is already in the tree, update its value
		if node != None:
			node.data = data
			return False
		
		# otherwise add a new entry
		
		
	
	def _search(self, subtree, target_key):
		
		# base case
		if subtree == None:
			return None
		
		# target is left of the subtree root
		elif target_key < subtree.key:
			return self._search(subtree.left, target_key)
		
		# target is right of the subtree root
		elif target_key > subtree.key:
			return self._search(subtree.right, target_key)
		
		# base case
		# the target is contained in the current node
		# returns a reference to the current node containing that key
		else:
			return subtree
			
	
		
	def _min(self, subtree):
		if subtree == None:
			return None
		elif subtree.left == None:
			return subtree
		else:
			return (self._min(subtree.left))

	def _max(self, subtree):
		if subtree == None:
			return None
		elif subtree.right == None:
			return subtree
		else:
			return (self._max(subtree.right))


'''


	def inorder(subtree)
	def preorder(subtree)
	def postorder(subtree)
	def _search(subtree, target_key)
	def _min(subtree)
	def _max(subtree)
	def __conatains__(key)
	def valueOf(key)
	
'''
