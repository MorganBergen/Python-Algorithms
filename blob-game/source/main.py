'''
@file		main.py
@author		Morgan Bergen
@date		April 24 2022
@brief		This file contains the main functon 
			The main function is in charge of 
			- calling upon constructing and initilaizing the Maze class.
			- reading in the characters of the input file.
			- running the path for the blob to spread.
			- revealing the final output.
'''


from maze import Maze

'''
@pre		None
@post		builds ADT Maze and prints out final output
@param		None
@raises		None
@returns	None
'''
def main():

	exec = Maze()
	exec.build_grid()
	exec.start()
	exec.print_final()

if __name__ == "__main__":
	main()
