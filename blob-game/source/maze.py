
class Maze:
	
	def __init__(self):
		self.file = ""
		self.total_rows = 0
		self.total_cols = 0
		self.start_row = 0
		self.start_col = 0
		self.total_eaten = 0
		self.grid = []
		
	def print_grid(self):
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				print(f"{self.grid[i][j]}", end="")
			print()
	def build_grid(self):
		x = False
		while x == False:
			# self.file = input("enter file: ")
			self.file = "1-input.txt"
			# self.file = "2-input.txt"
			x = self.fileio()
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
	def reset_grid(self):
		self.fileio()

	def find_path(self, row, col):
		return True

	def valid_move(self, row, col):
		return False