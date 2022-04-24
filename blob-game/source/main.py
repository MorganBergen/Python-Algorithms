
from maze import Maze


def main():
	m = Maze()
	m.build_grid()
	m.start()
	m.print_final()

if __name__ == "__main__":
	main()
