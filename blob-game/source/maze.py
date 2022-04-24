'''
@file		maze.py
@author		Morgan Bergen
@date		April 24 2022
@brief		This file contains all of the member variables and member methods implementations of the project.
			This Maze class does the following at a high level overview of it's job
			- it will request file input from the user
			- read in the characters and initialize the grid within a list of lists
			- determine if the file is valid or not
			- it will enumerate the number of sewers, people, total rows, total cols, start row and start col indexes.
			- the walk function will then use recursion for the blob to spread
				- helper methods such as mark and valid_spot are used to determine whether the blob should move or not
			- print_final will reveal to the user in a grid view the finalized blob in the city outcome
			
'''

class Maze:
	
	'''
	@pre		Maze() must be called outside this class
	@post		Member variables are initialized at their default values
	@param		None
	@raises		None
	@returns	None
	'''
	def __init__(self):
		self.file = ""
		self.total_rows = 0
		self.total_cols = 0
		self.start_row = 0
		self.start_col = 0
		self.total_eaten = 0
		self.total_ppl = 0
		self.total_sewers = 0
		self.sewer_row_locations = []
		self.sewer_col_locations = []
		self.grid = []
		self.track = 0
		self.cur = []

	'''
	@pre		build_grid() must be called
	@post		total_sewers is accurately initialized based on how many occurances of '@' are found from the input file
	@param		None
	@raises		None
	@returns	None
	'''
	def count_sewers(self):
		for row in self.grid:
			for value in row:
				if value == '@':
					self.total_sewers = self.total_sewers + 1

	'''
	@pre		build_grid() must be called
	@post		list variables sewer_row_locations and sewer_col_locations are accurately initialized based on the index position of '@'
	@param		None
	@raises		None
	@returns	None
	'''	
	def locate_sewers(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				if self.grid[i][j] == '@':
					self.sewer_row_locations.append(i)
					self.sewer_col_locations.append(j)

	'''
	@pre		start() must have already been called
	@post		prints out the grid, plus each characters corresponding index row and column position
	@param		None
	@raises		None
	@returns	None
	'''
	def print_grid(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				print(f" [{self.grid[i][j]}]{i}{j} ", end="")
			print()
 
	'''
	@pre		start() must have already been called
	@post		prints out the grid
	@param		None
	@raises		None
	@returns	None
	'''
	def print_simple(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				print(f"{self.grid[i][j]}", end="")
			print()



	'''
	@pre		start() must have already been called
	@post		calls print_simple() and prints important member variable values
	@param		None
	@raises		None
	@returns	None
	'''
	def print_info(self):
		print("__________grid__________")
		self.print_simple()
		print("__________info__________")
		print(f" total ppl {self.total_ppl}")
		print(f" total eaten {self.total_eaten}")
		print(f" total sewers {self.total_sewers}")
		print(f" sewer locals ", end="")
		for i in range(len(self.sewer_row_locations)):
			print(f"[{self.sewer_row_locations[i]}, {self.sewer_col_locations[i]}] ", end="")
		print("\n________________________________")

	'''
	@pre		start() must have already been called
	@post		prints the write up's preferred output of the grid
	@param		None
	@raises		None
	@returns	None
	'''
	def print_final(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				for k in range(len(self.sewer_row_locations)):
					if i == self.sewer_row_locations[k] and j == self.sewer_col_locations[k]:
						self.grid[i][j] = '@'
				print(f"{self.grid[i][j]}", end="")
			print()
		print(f"total eaten {self.total_eaten}")		

	'''
	@pre		Maze() must have already been constructed
	@post		initializes the file member variable from requesting input from the user
				if fileio works properly then count_pp(), count_sewers(), and locate_sewers() will all be called for initializing
				important information regarding the characters of the input file.
	@param		None
	@raises		None
	@returns	None
	'''
	def build_grid(self):
		x = False
		while x == False:
			self.file = input("enter file: ")
			x = self.fileio()
		self.total_ppl = self.count_ppl()
		self.sewers = self.count_sewers()
		self.locate_sewers()

	'''
	@pre		build_grid() must have allready been called
	@post		the input file is read in
				grid, total_rows, total_cols, start_row, start_col will all be initialized based on the file
				valid_dimenions() will be called in order to determine if the input file is legal
				- we assume the file is of the following format type
					<numRows> <numCols>
					<Blob startRow> <Blob startCol>
					<map characters>
				- FileNotFoundError will display a message indicates that the file is not located within current project directory
	@param		None
	@raises		FileNotFoundError
	@returns	True if the fileIO worked, False if otherwise
	'''
	def fileio(self):
		try:
			f = open(self.file, 'r')
		except FileNotFoundError as e:
			print(e)
			return False
		else:
			total = f.readline().split()
			start = f.readline().split()
			self.grid = list(f.read().splitlines())
			self.total_rows = int(total[0])
			self.total_cols = int(total[1])
			self.start_row = int(start[0])
			self.start_col = int(start[1])
			
			if self.valid_dimensions() == False:
				return False
			else:
				for i in range(len(self.grid)):
					self.grid[i] = list(self.grid[i])
		f.close()
		return True

	'''
	@pre		fileio() must have already been called
	@post		will determine if the dimensions of the file are accurate
				we assume the map characters match the parameters given from the file
	@param		None
	@raises		None
	@returns	True if the dimensions are valid
				False if the dimensions provided in the input file are invalid 
				- and displaying an error messaging indicating which dimension was invalid
				
				conditions for invaid dimensions:
				- if file doesn't exist
				- if numRows are less than 1
				- if numCols are less than 1
				- if start position is not within range

	'''
	def valid_dimensions(self):
		if self.total_rows < 1:
			print(f"error: invalid dimensions provided, total rows cannot be less than 1")
			return False
		elif self.total_cols < 1:
			print(f"error: invalid dimensions provided, total cols cannot be less than 1")
			return False
		elif self.start_row > self.total_rows:
			print(f"error: invalid dimensions provided, starting position is not within range.")
			return False
		elif self.start_col > self.total_cols:
			print(f"error: invalid dimensions provided, starting position is not within range.")
			return False
		elif self.start_col < 0:
			print(f"error: invalid dimensions provided, starting position is not within range.")
			return False
		elif self.start_row < 0:
			print(f"error: invalid dimensions provided, starting position is not within range.")
			return False
		else:
			return True
	
	'''
	@pre		None
	@post		will re-read the file again and reinitialize grid character and member variable values
	@param		None
	@raises		None
	@returns	None
	'''
	def reset_grid(self):
		self.fileio()

	'''
	@pre		build_grid() must have been called and fileio() must have returned True
	@post		counts the amount of people there are in the grid and returns that integer value
	@param		None
	@raises		None
	@returns	ppl
	'''
	def count_ppl(self):
		ppl = 0
		for i in range(len(self.grid)):
			ppl = self.grid[i].count('P') + ppl
		return (ppl)

	'''
	@pre		build_grid() must have been called correctly
	@post		The blob spreads through the grid
	@param		None
	@raises		None
	@returns	walk(start_row, start_col)
	'''
	def start(self):
		return (self.walk(self.start_row, self.start_col))

	'''
	@pre		start() must have been called
	@post		the blob will have moved throughout the grid
				self.cur is marked with the current index position that the walk is analyzing
				mark(row, col) will alter the grid's values based on the location of the grid
				track is used to track how many moves the blob took in order to recurse through the maze
				if the blob is allowed to move a recursive call will allow for the grid to be marked
					- valid_spot will check in the following order: up, right, down, left
					- if valid_spot() returns true then a recursive call in the direction will be made
				if the blob cannot move up, right, down, or left then the grid at the current position will be marked as 'B'
	@param		row, col
	@raises		None
	@returns	None
	'''
	def walk(self, row, col):
		
		# print(f" [{self.grid[row][col]}]{self.cur[0]}{self.cur[1]}")
		self.cur = [row, col]
		self.mark(row, col)
		self.track = self.track + 1
		
		if self.valid_spot(row - 1, col): #check up
			self.walk(row - 1, col)
		
		if self.valid_spot(row, col + 1): #check right
			self.walk(row, col + 1)

		if self.valid_spot(row + 1, col): #check down
			self.walk(row + 1, col)
		
		if self.valid_spot(row, col - 1): #check left last check
			self.walk(row, col - 1)	
		
		self.grid[row][col] = 'B'

	'''
	@pre		walk() must have been called
	@post		streets represented by capital 'S' 
				- so if the grid[row][col] is 'S' then it's marked as a integer 
				  which represents the current total number of moves the blob took in order to recurse throughout the maze
				people represented by capital 'P'
				- so if the grid[row][col] is 'P' then the grid is marked by track member variable
				- total eaten will be increamented by one
				buildings are represented by '#' 
				- so the blob cannot mark this position
				sewers are represented by '@'
				- all sewers are considered adjacent
				- if the blob has eaten all possible people and runs into a sewer, then the sewer will be marked as track
				- else then the sewer will be marked as it was prior '@'
	@param		None
	@raises		None
	@returns	None if it can mark on a valid character, False if otherwise
	'''
	def mark(self, row, col):
		
		if self.grid[row][col] == 'P':
			self.total_eaten = self.total_eaten + 1
			self.grid[row][col] = self.track
		elif self.grid[row][col] == 'S':
			self.grid[row][col] = self.track
		elif self.grid[row][col] == '@':
			if self.total_ppl == self.total_eaten:
				self.grid[row][col] = self.track
			else:
				self.grid[row][col] = '@'	
		else:
			return False

	'''
	@pre		walk(row, col) must have already been called
	@post		checks if the blob can move
				if it encounters a '@' aka a sewer space and 
				 - it has tried to spread in all other directions, 
				 - it will spread into the sewer, which allows it to move to all connected sewer spaces one at a time
				 - once the Blob moves through a sewer it continues to move as normal
				 - walk(row, col) will be called based on the next located sewer space
	@param		row, col		
	@raises		None
	@returns	True if the move is valid, false if otherwise
	'''
	def valid_spot(self, row, col):
		if row >= 0 and row < self.total_rows and col >= 0 and col < self.total_cols:
			if self.grid[row][col] == 'P':
				return True
			elif self.grid[row][col] == 'S':
				return True
			elif self.grid[row][col] == '@':
				for i in range(self.total_sewers):
					if row == self.sewer_row_locations[i] and col == self.sewer_col_locations[i]:
						if i == 0 and self.total_sewers > 1:
							self.walk(self.sewer_row_locations[i+1], self.sewer_col_locations[i+1])
						elif i == 0 and self.total_sewers == 1:
							self.walk(self.sewer_row_locations[i], self.sewer_col_locations[i])
						elif i == self.total_sewers - 1:
							self.walk(self.sewer_row_locations[i-1], self.sewer_col_locations[i-1])
						elif i > 0 and i <= self.total_sewers - 1:
							self.walk(self.sewer_row_locations[i+1], self.sewer_col_locations[i+1])
				return True
			else:
				return False
		else:
			return False