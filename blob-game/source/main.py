
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
	m.find_path(m.start_row, m.start_col)
	m.print_grid()

main()