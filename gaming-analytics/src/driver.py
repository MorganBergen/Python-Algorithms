'''
@file		driver.py
@author		Morgan Bergen
@date		February 4 2022
@brief		This file contains the main function.
			The main takes a file input from the user.
			Then generates an object and hands off control off to the executive class.
'''

from executive import Executive

def main():
	file_name = input("Enter the name of the input file: ")
	my_exec = Executive(file_name)
	my_exec.run()

if __name__ == "__main__":
	main()
