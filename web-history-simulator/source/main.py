'''
@file		main.py
@author		Morgan Bergen
@date		March 11 2022
@brief		This main fuction is the primary drive for which all other member methods and classes are called from.  The user is prompted to enter an input.txt file, if the user does not properly enter a input.txt file then they will be requested to input their string again.
'''

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
