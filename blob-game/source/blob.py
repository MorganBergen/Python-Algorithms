from map import Map

class Blob:
	
	def __init__(self):
		self.city = Map()
		self.city.allocate()
		
	def print(self):
		for i in range(self.city.num_rows):
			for j in range(self.city.num_cols):
				print(f"city.")
			
	
#	def print(self):
#		print(slecity)
#		for i in range(city.map.num_rows):
#			for j in range(city.map.num_cols):
#				print(f"{city[i][j]}", end="")
#			print()
#	def print(self):
#		print("\nmap")
#		for i in range(self.r):
#			for j in range(self.c):
#				if i == self.sr and j == self.sc:
#					print(f"B", end="")
#				else:
#					print(f"{self.map[i][j]}", end="")
#			print()
	
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
		
#	def move(self, row, col):












