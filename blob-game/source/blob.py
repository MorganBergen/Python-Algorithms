from map import Map

class Blob:
	
	def __init__(self):
		self.city = Map()
		self.city.allocate()
		
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
		if self.map[row][col] == "S":
			return True
		elif self.map[row][col] == "P":
			return True
		elif self.map[row][col] == "@":
			return True
		elif self.map[row][col] == "#":
			return False
		else:
			return False
		
	def move(self):
		self.city.set_element(self.city.start_row, self.city.start_col, "B")
		






