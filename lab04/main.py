
from linkedlist import LinkedList

def main():
	list = LinkedList()
	print(f"length == {list.get_length()}")
	
	try:
		list.insert(0, "http://google.com")
		list.insert(0, "http://reddit.com")
	except IndexError as e:
		print(e)
		
	print(list._front.data)
	print(list._front.next)
	print(f"length == {list.get_length()}")

if __name__ == "__main__":
	main()


'''
1. implement LL
2. implement LL using browser
'''
