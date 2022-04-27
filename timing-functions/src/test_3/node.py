'''
@file		node.py
@author		Morgan Bergen
@date		March 4 2022
@brief		This is the Node class.
			The nodes are the atomic building blocks of the queue data structure.
			each node consists of data and a references to the next node.
'''

class Node:
	
	'''
	@pre		Queue object must be constructed
	@post		self.next is initially refered to none
	@param		data
	@raises		None
	@returns	None
	'''
	def __init__(self, data):
		self.data = data
		self.next = None
