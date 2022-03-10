
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
		list.set_entry(0, "NEW ENTRY")
	except IndexError as mee:
		print("\n", mee, "\n")
	
	print_list(list)
	print()
	
	
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
