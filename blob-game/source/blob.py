from map import Map

class Blob:
	
	def __init__(self):
		map = Map()
		map.allocate()
		
		# storage
		self.r = map.num_rows
		self.c = map.num_cols
		self.sr = map.start_row
		self.sc = map.start_col
		self.map = map.map
	
	def change(self, x):
		if x == 0:
			print(x)
			return 0
		else:
			print(x)
			return self.change(x-1)

	def traverse(self):
		for i in range(self.r):
			if i == self.r:
				for j in range(self.c):
					if j == self.c:
						print(f"{self.map[self.r][self.c]}", end="")
					else:
						print(f"{self.map[i][j]}", end="")
			else:
				for j in range(self.c):
					print(f"{self.map[i][j]}", end="")
			print()
	
		






















