

from bisect import insort
from tree import Tree



def main():

	tree = Tree()
	tree.add(1, "a")
	tree.add(2, "b")
	tree.add(3, "c")
	tree.add(4, "d")
	tree.add(5, "e")
	tree.add(6, "f")

	try:
		tree.add(1, "string")
	except RuntimeError as e:
		print(e)
	
	tree.inorderTrav(tree.root)
	
	


if __name__ == "__main__":
	main()
	

'''
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
'''