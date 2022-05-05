
from tree import Tree
from node import Node

#include <iostream>

def main():
	
	tree = Tree()
	tree.build()
	print(tree._search(tree.root, 71).data)
	
	print(90 in tree)
	
	print(f"{tree.root.left.left.key} is {tree.root.left.left.data} ")
	
	
	print("did we add a new node?")
	
	state = tree.add(4, "NEW DATA")
	if state == False:
		print(f"{tree.root.left.left.key} is {tree.root.left.left.data} ")
	else:
		print("error")
	
	next = tree.add(3, "new node")
	
	if next == True:
		print(f"{tree.root.left.left.right.key} is {tree.root.left.left.right.data} ")
	else:
		print("error")
		
	std::cout << "hello my name is morgan" << std::endl;


if __name__ == "__main__":
	main()
