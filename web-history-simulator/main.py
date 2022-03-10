
from linkedlist import LinkedList

def main():
	list = LinkedList()
	print()
	
	try:
		list.insert(0, "http://google.com")
		list.insert(1, "https://reddit.com")
		list.insert(2, "http://facebook.com")
		list.insert(3, "http://myspace.com")
	except IndexError as e:
		print(e)
		
	print_list(list)
	print()
	
	try:
		list.remove(0)
		print()
	except RuntimeError as foo:
		print(foo)
		
	except IndexError as bar:
		print(bar)
	
	print_list(list)
	
	list.clear()
	
	print()
	print_list(list)
	
	try:
		list.remove(100)
	except IndexError as p:
		print(p)
	except RuntimeError as e:
		print(e)
	
	
def print_list(original):
	if original.is_empty():
		print("list empty")
	else:
		for i in range(original.get_length()):
			print(f"{i} -> ", end="")
		print()
		for i in range(original.get_length()):
			print(f"{original.get_entry(i)} -> ", end="")
	
	
if __name__ == "__main__":
	main()


'''
1. implement LL
2. implement LL using browser
'''
