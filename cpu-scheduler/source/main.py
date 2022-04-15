'''
@file		main.py
@author		Morgan Bergen
@date		March 4 2022
@brief		This is the main module
			This acts as a driver for all other functions and classes to be run from.
			Main initially asks the user for the name of the input file.
			Then thereafer it generates one executive object which is of class type CPU and runs the fileIO(file_name) function to organize and feed in the input data into the correct data data structure.
'''

from cpu_scheduler import Cpu

'''
	@pre		user must input a valid existent file name.
	@post		the Cpu object is initialized and conructed and the file from the user is read in by Cpu()'s member method fileIO
	@param		None
	@raises		None
	@returns	None
	'''
def main():
	file_name = input("Enter the name of the input file: ")
	exec = Cpu()
	exec.fileIO(file_name)

if __name__ == "__main__":
	main()
