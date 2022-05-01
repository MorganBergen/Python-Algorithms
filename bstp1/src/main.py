
from  node import Node

def main():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	
	print(f"	[{root.data}]")
	print(f"	/ \	")
	
if __name__ == "__main__":
	main()
	
