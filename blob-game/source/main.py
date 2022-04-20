
from maze import Maze


def build_reset_test():
	city = Maze()
	city.build_grid()
	city.print_grid()
	print("_____________________________")
	city.grid[0][0] = "B"
	print(f"first instance of 'S' at 0 {city.grid[0].index('S')}")
	city.print_grid()
	print("_____________________________")
	city.reset_grid()
	city.print_grid()
	print("_____________________________")
	return None


def main():
	
	build_reset_test()

main()


'''

class Maze:
	
	def __init__(self):
		self.file = ""
		self.total_rows = 0
		self.total_cols = 0
		self.start_row = 0
		self.start_col = 0
		self.grid = []
		
	def print_memebers(self):
		print(f"self.file = {self.file}")
		print(f"self.total_rows = {self.total_rows}")
		print(f"self.total_cols = {self.total_cols}")
		print(f"self.start_row = {self.start_row}")
		print(f"self.start_col = {self.start_col}")
		print(f"self.grid = {self.grid}")
		
	def build_grid(self):
		x = False
		while x == False:
			self.file = input("enter file: ")
#			self.file = "1-input.txt"
#			self.file = "2-input.txt"
			x = self.fileio()
			
	def fileio(self):
		try:
			f = open(self.file, 'r')
		except FileNotFoundError as e:
			print(e)
			return False
		else:
			total = f.readline()
			start = f.readline()
			self.grid = list(f.read().splitlines())
			
			x = total.split()
			y = start.split()
			
			print(f"row and col {x}")
			print(f"start row and col {y}")
			
			self.total_rows = int(x[0])
			self.total_cols = int(x[1])
			self.start_row = int(y[0])
			self.start_col = int(y[1])
			
			
			
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
		
'''
