
from tree import Tree

def test():
	tree = Tree()
	
	tree.insert(60, "a")
	tree.insert(25, "b")
	tree.insert(100, "c")
	tree.insert(35, "d")
	tree.insert(17, "e")

	print("pre-order traversal")
	tree.preorder(tree.root)

	print("in-order traversal")
	tree.inorder(tree.root)

	print("post-order traversal")
	tree.postorder(tree.root)

def main():
	print("working")

if __name__ == "__main__":
	main()
