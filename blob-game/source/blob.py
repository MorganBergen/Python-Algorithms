from map import Map

class Blob:
	
	def __init__(self):
		self.city = Map()
		self.city.allocate()
		self.counter = 0
		self.exaustive_search = 0
	
	def print(self):
		for i in range(len(self.city.map)):
			for j in range(len(self.city.map[i])):
				print(f" {self.city.get_element(i, j)}  ", end="")
			print()
		print()
	
	def indexes(self):
		for i in range(self.city.num_rows):
			for j in range(self.city.num_cols):
				print(f" {i}{j} ", end="")
			print()
		print()
	
	def is_valid_move(self, row, col):
		
		if row >= self.city.num_rows or row < 0 or col >= self.city.num_cols or col < 0:
			print(f" check [{row}][{col}]")
			return False
		else:
			print(f" check [{row}][{col}]")
			temp = self.city.get_element(row, col)
			print(f" temp = {temp}")
			
			if temp == "S":
				return True
			elif temp == "P":
				return True
			elif temp == "@":
				return True
			elif temp == "#":
				return False
			else:
				return False
	
	def start(self):
		self.city.set_element(self.city.start_row, self.city.start_col, "B")
	
	def move(self, row, col):
		row = int(row)
		col = int(col)
		exaustive_search = 0
		
		if row < 0 or col < 0:
			return False
		elif row > self.city.num_rows or col > self.city.num_cols:
			return False
		else:
			
			print(f" [{row}][{col}] {self.mark(row, col)}->{self.city.map[row][col]}")
			self.print()
			
			if self.is_valid_move(row - 1, col):
				self.exaustive_search = self.exaustive_search + 1
				return (self.move(row - 1, col))
				
			elif self.is_valid_move(row, col + 1):
				self.exaustive_search = self.exaustive_search + 1
				return (self.move(row, col + 1))
			
			elif self.is_valid_move(row + 1, col):
				self.exaustive_search = self.exaustive_search + 1
				return (self.move(row + 1, col))
			
			elif self.is_valid_move(row, col - 1):
				exaustive_search = self.exaustive_search + 1
				return (self.move(row, col - 1))
			
			elif self.exaustive_search == 4:
				return False
				
			else:
				return False
			
		
#
#	def mark(self, row, col):
#		prev = self.city.map[row][col]
		
	
	
	def mark(self, row, col):
		previous = self.city.map[row][col]
		self.city.map[row][col] = self.counter
		self.counter = self.counter + 1
		if previous != None:
			return(previous)








