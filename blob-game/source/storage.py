

'''
@file       main.py
@author     Morgan Bergen
@date       April 14 2022
@brief      the executive main which calls upon the input.txt file
'''

def main():
	
	run = True
	while run:
		f_name = input("enter file name: ")
		run = fileIO(f_name)
	else:
		print("worked")
		

def fileIO(file):
	run = True
	while run:
		try:
			fo = open(file, 'r')
		except FileNotFoundError as e:
			print(e)
		finally:
			run = False
			print("name of file is ", fo.name)
			dimensions = fo.readline().split()
			start_dimensions = fo.readline().split()
			numRows = dimensions[0]
			numCols = dimensions[1]
			startRow = start_dimensions[0]
			startCol = start_dimensions[1]
			map = fo.read().splitlines()
			print(f"startRow = {startRow}")
			print(f"startCol = {startCol}")
			print(f"numRows = {numRows}")
			print(f"numCols = {numCols}")
			print(map)
			fo.close()
	else:
		return(False)


'''
invalid file if the file does not exit
if numRows are less than 1
if numCols are less than 1
if start position is not within range
'''
		
		


main()
