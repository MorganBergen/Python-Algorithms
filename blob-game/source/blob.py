from map import Map

class Blob:
	
	def __init__(self):
		self.city = Map()
		self.city.allocate()
		# move counter
		self.counter = 0
#		self.new = []
		
	def print(self):
		for i in range(self.city.num_rows):
			for j in range(self.city.num_cols):
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
			if self.city.get_element(row, col) == "S":
				return True
			elif self.city.get_element(row, col) == "P":
				return True
			elif self.city.get_element(row, col) == "@":
				return True
			elif self.city.get_element(row, col) == "#":
				return False
			else:
				return False
		
	def start(self):
		self.city.set_element(self.city.start_row, self.city.start_col, "B")
		
		
	def move(self, row, col):
		print(f"row {row}")
		print(f"col {col}")
		if row < 0 or col < 0:
			return False
		else:
			self.mark(row, col)
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
				return True
			
		
			
		
	def mark(self, row, col):
		previous = self.city.map[row][col]
		self.city.map[row][col] = self.counter
		self.counter = self.counter + 1
		return(previous)
		























