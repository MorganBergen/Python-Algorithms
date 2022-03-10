
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
		list.remove(2)
		print()
	except RuntimeError as e:
		print(e)
	print()
	
	print_list(list)
	
	
def print_list(original):
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
