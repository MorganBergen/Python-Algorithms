'''
@file 	map.py
@author	Morgan Bergen
@date 	April 14 2022
@brief	the map class which handle initial file io
  fileIO
  will allocate memory into member variables from the input file fed in by the user
  edge cases:
  - if file doesn't exist, then  fileIO will catch an exception if the file does not exit and terminate the program
  - if numRows are less than 1, if numCols are less than 1, and or if start position is not within range then generate an error message and terminate the program
'''

from string import *

class Map:
	
	def __init__(self):
		self.file = ""
		self.num_rows = 0
		self.num_cols = 0
		self.start_row = 0
		self.start_col = 0
		self.map = []
	
#	self.file = input("file name: ")
	def allocate(self):
		stop_running = False
		while stop_running == False:
#			self.file = input("file name: ")
			self.file = "input.txt"
			stop_running = self.fileIO()
	
	def fileIO(self):
		try:
			stream = open(self.file, 'r')
		except FileNotFoundError("error: file nost, found please try again."):
			print(e)
			return False
		else:
			dim = stream.readline().split()
			start = stream.readline().split()
			
			self.map = list(stream.read().splitlines())
		
			self.num_rows = int(dim[0])
			self.num_cols = int(dim[1])
			self.start_row = int(start[0])
			self.start_col = int(start[1])
			
			if self.num_rows < 1 or self.num_cols < 1:
				print("error: invalid map dimensions")
				return False
			elif self.start_row > self.num_rows or self.start_col > self.num_cols:
				print("error: start position is not within range")
				return False
			
			for i in range(len(self.map)):
				self.map[i] = list(self.map[i])
				
		stream.close()
		return True
	
	def	get_element(self, row, col):
		row = int(row)
		col = int(col)
		return self.map[row][col]
	
	def set_element(self, row, col, element):
		row = int(row)
		col = int(col)
		self.map[row][col] = element
		
			
		
	
