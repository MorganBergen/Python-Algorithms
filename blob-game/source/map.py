
class Map:
	
	def __init__(self):
		self.file = ""
		self.num_rows = 0
		self.num_cols = 0
		self.start_row = 0
		self.start_col = 0
		self.map = []
		print(f"constructor has been called {self.file}")
	
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
			map = stream.read().splitlines()
			
			self.num_rows = dim[0]
			self.num_cols = dim[1]
			self.start_row = start[0]
			self.start_col = start[1]
			
			print(f"{self.num_row} {self.num_col}")
			print(f"{self.start_row} {self.start_col}")
			print(f"{map}\n{type(map)}")
			
			if self.num_rows < 1 or self.num_cols < 1:
				print("error: invalid map dimensions")
				return False
			elif self.start_row > self.num_rows or self.start_col > self.num_cols:
				print("error: start position is not within range")
				return False
			
			
