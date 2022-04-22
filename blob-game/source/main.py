
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

def test1():
	m = Maze()
	m.build_grid()
	m.start()

def main():


	test1()



if __name__ == "__main__":
	main()
