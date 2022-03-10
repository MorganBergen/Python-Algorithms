
from linkedlist import LinkedList

def main():
	list = LinkedList()
	print(f"length == {list.get_length()}")
	
	try:
		list.insert(0, "http://google.com")
	except IndexError as e:
		print(e)
		
	print(f"{list._front.data} -> ")
	print(f"length == {list.get_length()}")

	try:
		list.insert(1, "https://reddit.com")
	except IndexError as e:
		print(e)
		
	print(f"{list._front.data} -> {list._back.data}")
	
if __name__ == "__main__":
	main()


'''
1. implement LL
2. implement LL using browser
'''
