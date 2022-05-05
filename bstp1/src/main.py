
from tree import Tree

def main():
	
	me = Tree()
	me.build()
	print(me._search(me.root, 71).data)
	
	print(90 in me)


if __name__ == "__main__":
	main()
