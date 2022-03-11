
from browser import Browser
from executive import Executive

def main():
	file = input("Enter input file:  ")
	while file != "input.txt":
		print(f"ERROR: No file found titled {file}")
		file = input("Please Re-enter input file:  ")
		run = Executive(file)
		
	run = Executive(file)

if __name__ == "__main__":
	main()
