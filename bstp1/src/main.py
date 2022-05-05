
from tree import Tree
from node import Node

def main():
	
	tree = Tree()
	

	for i in range(100):
		tree.add(i, i)

	print(tree.root.data)

	

if __name__ == "__main__":
	main()
