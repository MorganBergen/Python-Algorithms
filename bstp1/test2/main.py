from tree import Tree

def main():
	tree = Tree()	

	
	tree.add(25, "25")
	tree.add(100, "100")
	tree.add(35, "35")
	tree.add(60, "60")
	tree.add(17, "17")
	tree.add(80, "80")
	tree.add(30, "30")

	print(tree.root.key, tree.root.data)

	print("inorder")
	tree.inorder(tree.root)

	print("preorder")
	tree.preorder(tree.root)

	print("postorder")
	tree.postorder(tree.root)


if __name__ == "__main__":
	main()
	
