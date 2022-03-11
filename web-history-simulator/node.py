'''
@file		node.py
@author		Morgan Bergen
@date		March 11 2022
@brief		This node class is the building blocks of what will make up the linkedlist.  Because this is a node based implementation of a linkedlist data structure, the member variables of the Node class consist of a data entry and a next which is intended to refer to the next node in the data structure.
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
