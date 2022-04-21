
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

def test():
	m = Maze()
	m.build_grid()
	m.start()
	m.print_grid()
	m.find_path(0, 2)
	print(f"total eaten = {m.total_eaten}")
	print(f"total people = {m.total_ppl}")
	print("_______")
	print(f"total eaten = {m.total_eaten}")
	print(f"total people = {m.total_ppl}")
	m.print_grid()

def main():

	m = Maze()
	m.build_grid()
	print("_____")
	m.print_grid()
	print("_____")
	m.start()
	m.print_grid()
	print("_____")

main()


'''
main.py
maze.py
'''



'''



# def start(self):
	# 	self.total_ppl = self.count_ppl()
	# 	if self.grid[self.start_row][self.start_col] == 'P':
	# 		self.total_eaten = self.total_eaten + 1
	# 	else:
	# 		self.grid[self.start_row][self.start_col] = '1'
			
	
	# row 0 col 2
	# def find_path(self, row, col):
	# 	if self.valid_move(row - 1, col):				# up
	# 		if self.mark_path(row - 1, col):
	# 			return (self.find_path(row - 1, col))
	# 	elif self.valid_move(row, col + 1): 			#right
	# 		if self.mark_path(row, col + 1):
	# 			return (self.find_path(row, col + 1))
	# 	elif self.valid_move(row + 1, col):				#down
	# 		if self.mark_path(row + 1, col):
	# 			return self.find_path(row + 1, col)
	# 	elif self.valid_move(row, col - 1):				#left
	# 		if self.mark_path(row, col - 1):
	# 			return self.find_path(row, col - 1)
	# 	else:
	# 		self.grid[row][col] = "B" #MARKING TWICE
	# 		if self.total_eaten == self.total_ppl:
	# 			print("recursive base case stop here")
	# 			return False
	# 		else:
	# 			return False

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