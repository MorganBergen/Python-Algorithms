
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

	m = Maze()
	m.build_grid()

	m.start()

	m.print_grid()
	m.find_path(0, 2)

	print("_______")
	print(f"total eaten = {m.total_eaten}")
	print(f"total people = {m.total_ppl}")
	m.print_grid()



main()


'''
old funcyion definition
def valid_move(self, row, col):
		if self.valid_position(row, col):
			x = self.grid[row][col]
			if x == 'S':
				return True
			elif x == 'P':
				self.total_eaten = self.total_eaten + 1
				return True
			elif x == '#':
				return False
			else:
				if x == '1':
					return True
				elif x == '2':
					return True
				elif x == '3':
					return True
				elif x == '4':
					return True
				elif x == 'B':
					return False
		else:
			return False

	def valid_position(self, row, col):
		if self.total_rows <= row:
			return False
		elif self.total_cols <= col:
			return False
		elif row < 0:
			return False
		elif col < 0:
			return False
		else:
			return True


	def mark_path(self, row, col):
		x = self.grid[row][col]

		if x == '1':
			self.grid[row][col] = '2'
			return True
		elif x == '2':
			self.grid[row][col] = '3'
			return True
		elif x == '3':
			self.grid[row][col] = '4'
			return True
		elif x == '4':
			self.grid[row][col] = 'B' #WE MUST MOVE THIS? MARK AS 5 AND THEN?
			return True 
		else:
			self.grid[row][col] = '1'
			return True			
'''