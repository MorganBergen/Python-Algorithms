
from tree import Tree
from node import Node

def main():
	
	tree = Tree()
	

	tree.add(60, "a")
	tree.add(25, "b")
	tree.add(100, "c")
	tree.add(35, "d")
	tree.add(17, "e")

	try:
		tree.add(17, "e")
	except RuntimeError as e:
		print(e)
	
	

if __name__ == "__main__":
	main()
