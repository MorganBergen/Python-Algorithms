
from linkedlist import LinkedList

def main():
	list = LinkedList()
	print(list.length())
	
	try:
		list.insert(0, "http://google.com")
	except IndexError as e:
		print(e)
		
	print(list._front.data)
	print(list._front.next)

if __name__ == "__main__":
	main()


'''
1. implement LL
2. implement LL using browser
'''
