
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
	def inorder(self, subtree): #LVR
		self.inorder(subtree.left)
		print(subtree.key)
		self.inorder(subtree.right)
		
	# left, right, visit
	def postorder(self, subtree):
		self.postorder(subtree.left)
		self.postorder(subtree.right)
		print(subtree.key)
