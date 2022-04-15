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

class Map:
	
	def __init__(self):
		self.file = ""
		self.num_rows = 0
		self.num_cols = 0
		self.start_row = 0
		self.start_col = 0
		self.map = []
	
	def run(self):
		run = False
		while run == False:
			self.file = input("file name: ")
			run = self.fileIO()
			
	def fileIO(self):
		try:
			stream = open(self.file, 'r')
		except FileNotFoundError("error: file nost, found please try again."):
			print(e)
			return False
		else:
			dim = stream.readline().split()
			start = stream.readline().split()
			self.map = stream.read().splitlines()
			
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
			
		stream.close()
		return True
		
		
	def printMap(self):
		
		print(f"{self.num_rows} {self.num_cols}")
		print(f"{self.start_row} {self.start_col}")
		
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				print(f"{self.map[i][j]}", end="")
			print()
			
			
			
			
			
			
			
			
			
			
			
			
