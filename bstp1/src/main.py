from tree import Tree

def main():
	tree = Tree()	

	for i in range(5):
		try:
			tree.add(i, i)
		except RuntimeError as e:
			print(e)

	print(tree.root.key)


if __name__ == "__main__":
	main()
	
