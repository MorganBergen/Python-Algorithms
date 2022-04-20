from map import Map

class Blob:
	
	def __init__(self):
		self.city = Map()
		self.city.allocate()
		self.counter = 0
		
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
		
		if row > self.city.num_rows or row < 0:
			return False
		elif col > self.city.num_cols or col < 0:
			return False
		else:
			temp = self.city.get_element(row, col)
			print(f" {temp} ", end="")
			if temp == "S":
				return True
			elif temp == "P":
				return True
			elif temp == "@":
				return True
			elif temp == "#":
				return False
			elif self.counter - temp > 0:
				return True
			else:
				return False
		
	def start(self):
		self.city.set_element(self.city.start_row, self.city.start_col, "B")
		
	def move(self, row, col):
		row = int(row)
		col = int(col)
		print(f"{row}{col}")
		
		if row < 0 or col < 0:
			return False
		elif row > self.city.num_rows or col > self.city.num_cols:
			return False
		else:
			print(f" {self.mark(row, col)} -> {self.city.map[row][col]}")
			self.print()
			
			if self.is_valid_move(row - 1, col):
				
				return (self.move(row - 1, col))
				
			elif self.is_valid_move(row + 1, col):
				
				return (self.move(row + 1, col))
				
			elif self.is_valid_move(row, col - 1):
				
				return (self.move(row, col - 1))
				
			elif self.is_valid_move(row, col + 1):
				
				return (self.move(row, col + 1))
				
			else:
				return False
			
	def mark(self, row, col):
		previous = self.city.map[row][col]
		self.city.map[row][col] = self.counter
		self.counter = self.counter + 1
		if previous != None:
			return(previous)
			
		























