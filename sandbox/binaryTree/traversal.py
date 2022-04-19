
from node import Node

class traversal:
	def __init__(self, data):
		self.node= Node(data)
		

	def preorderTrav(self, subtree):
		if subtree is not None:
			print(subtree.data)
			preorderTrav(subtree.left)
			preorderTrav(subtree.right)

	def inorderTrav(self, subtree):
		if subtree is not None:
			inorderTrav(subtree.left)
			print(subtree.data)
			inorderTrav(subtree.right)
	
	def postorderTrav(self, subtree):
		if subtree is not None:
			postorderTrav(subtree.left)
			postorderTrav(subtree.right)
			print(subtree.data)
			
