'''
@file		node.py
@author		Morgan Bergen
@date		March 4 2022
@brief		This is the Node class
			Consisting of data and a refesrence to the next node, initially constructed with self.next refering to none.
'''

class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None
