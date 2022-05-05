
from tree import Tree
from node import Node

def tester():
	tree = Tree()
	tree.add(2)
	tree.print_tree()
	
	tree.add(1)
	tree.add(3)
	
	tree.print_tree()
	return None

def main():
	
	root = Node(1)
	root.right = Node(2)
	root.left = Node(0)

	inorderTrav(root)
	

def inorderTrav(subtree):
	if subtree != None:
		inorderTrav(subtree.left)
		print(subtree.data)
		inorderTrav(subtree.right)
	

	
if __name__ == "__main__":
	main()
	

